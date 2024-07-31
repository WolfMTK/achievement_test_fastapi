from collections.abc import Iterator
from typing import Any

from sqlalchemy import (
    insert,
    select,
    ScalarResult,
    desc,
    true,
    func,
    case,
    CTE,
    CursorResult
)

from app.adapter.sqlalchemy_db.models import (
    UsersAchievements,
    Users,
    Achievements
)
from app.adapter.stubs.achievement_user import StubAchievementUserGateway
from app.domain.models import UserId, AchievementId
from .base import BaseGateway

LIMIT = 1


class AchievementUserGateway(BaseGateway, StubAchievementUserGateway):
    async def get_achievements(
            self,
            user_id: UserId,
            limit: int,
            offset: int
    ) -> ScalarResult[UsersAchievements]:
        """
        Получение достижений пользователя.

        SELECT
            ua.user_id,
            ua.achievement_id,
            ua.date_one
        FROM
            users_achievements AS ua
        LIMIT
            $1
        OFFSET
            $2
        """
        stmt = select(UsersAchievements).limit(limit).offset(offset).where(
            UsersAchievements.user_id == user_id
        )
        result = await self.session.execute(stmt)
        return result.scalars()

    async def create(
            self,
            user_id: UserId,
            achievement_id: AchievementId
    ) -> UsersAchievements:
        """
        Добавить достижения пользователю

        INSERT INTO
            users_achievements (user_id, achievement_id)
        VALUES
            ($1, $2)
        """
        stmt = insert(UsersAchievements).values(
            user_id=user_id,
            achievement_id=achievement_id,
        ).returning(UsersAchievements)
        result = await self.session.execute(stmt)
        return result.scalar()

    async def check_user_id_and_achievement_id(
            self,
            user_id: UserId,
            achievement_id: AchievementId
    ) -> bool:
        """
        Проверить user_id и achievement_id.

        SELECT EXISTS (
            SELECT
                u.id,
                u.name,
                u.language,
                a.id,
                a.name,
                a.number_points,
                a.description
            FROM
                users AS u
            JOIN
                achievements AS a ON u.id = $1 AND a.id = $2
        )
        """
        stmt = select(Users, Achievements).join(
            Achievements,
            (Users.id == user_id) & (Achievements.id == achievement_id)
        ).exists()
        return await self.session.scalar(select(stmt))

    async def check_achievement_user(
            self,
            user_id: UserId,
            achievement_id: AchievementId
    ) -> bool:
        """
        Проверка наличия достижения у пользователя.

        SELECT
            ua.user_id,
            ua.achievement_id,
            us.date_on
        FROM
            users_achievements
        WHERE
            ua.user_id = $1 AND ua.achievement_id = $2
        """
        stmt = select(UsersAchievements).where(
            UsersAchievements.user_id == user_id,
            UsersAchievements.achievement_id == achievement_id
        ).exists()
        return await self.session.scalar(select(stmt))

    async def get_total_achievements(self, user_id: UserId) -> int:
        """
        Получить количество достижений пользователя.

        SELECT
            COUNT(ua.achievement_id)
        FROM
            users_achievements AS ua
        WHERE
            us.user_id = $1
        """
        stmt = select(func.count(UsersAchievements.achievement_id)).where(
            UsersAchievements.user_id == user_id
        )
        return await self.session.scalar(stmt)

    async def get_max_achievements_user(
            self
    ) -> tuple[UserId, str, int] | None:
        """
        Получить пользователя с максимальным количеством достижений.

        SELECT
            u.id,
            u.name,
            count(ua.achievement_id) AS achievement_count
        FROM
            users AS u
        JOIN
            users_achievements AS ua ON u.id = ua.user_id
        GROUP BY
            u.id,
            u.name
        ORDER BY
            achievement_count DESC
        LIMIT
            1
        """
        stmt = (
            select(
                Users.id, Users.name, func.count(
                    UsersAchievements.achievement_id
                ).label('achievement_count')
            )
            .join(UsersAchievements, Users.id == UsersAchievements.user_id)
            .group_by(Users.id, Users.name)
            .order_by(desc('achievement_count'))
            .limit(LIMIT)
        )
        result = await self.session.execute(stmt)
        result_first = result.first()
        if result_first is None:
            return None
        return result_first.tuple()

    async def check_user_exists(self, user_id: UserId) -> bool:
        """
        Проверить, что пользователь существует.

        SELECT EXISTS (
            SELECT
                *
            FROM
                users AS u
            WHERE
                u.id = $1
        )
        """
        stmt = select(Users).where(Users.id == user_id).exists()
        return await self.session.scalar(select(stmt))

    async def get_max_achievement_points_user(
            self
    ) -> tuple[UserId, str, int] | None:
        """
        Получить пользователя с максимальным количеством очков достижений.

        SELECT
            u.id,
            u.name,
            SUM(a.number_points) AS total
        FROM
            users AS u
        JOIN
            users_achievements AS ua ON u.id = ua.user_id
        JOIN
            achievements AS a ON a.id = ua.achievement_id
        GROUP BY
            u.id,
            u.name
        ORDER BY
            total DESC
        LIMIT
            1
        """
        stmt = (
            select(
                Users.id, Users.name, func.sum(
                    Achievements.number_points
                ).label('total')
            )
            .join(UsersAchievements, Users.id == UsersAchievements.user_id)
            .join(Achievements, Achievements.id == UsersAchievements.achievement_id)
            .group_by(Users.id, Users.name)
            .order_by(desc('total'))
            .limit(LIMIT)
        )
        result = await self.session.execute(stmt)
        result_first = result.first()
        if result_first is None:
            return None
        return result_first.tuple()

    async def get_users_with_max_points_diff(
            self
    ) -> Iterator[tuple[UserId, str, int, int]] | None:
        """
        Получение пользователей с максимальной разностью очков достижений.

        WITH user_points AS (
            SELECT
                u.id,
                u.name,
                SUM(a.number_points) AS total
            FROM
                users AS u
            JOIN
                users_achievements AS ua ON u.id = ua.user_id
            JOIN
                achievements AS a ON a.id = ua.achievement_id
            GROUP BY
                u.id,
                u.name
        ),
        points_range AS (
            SELECT
                MAX(total) AS max_points,
                MIN(total) AS min_points
            FROM
                user_points
        )
        SELECT
            u.id,
            u.name,
            up.total,
            (points_range.max_points - points_range.min_points) AS max_diff
        FROM
            user_points AS up
        CROSS JOIN
            points_range
        WHERE
            up.total = points_range.max_points
            OR
            up.total = points_range.min_points
        """

        # Учитывал, что данных может быть большое количество,
        # вычисления перенес на сторону БД.

        user_points = self._get_max_points_user()
        points_range = self._get_points_range(user_points)

        stmt = (
            select(
                user_points.c.id,
                user_points.c.name,
                user_points.c.total,
                (
                        points_range.c.max_points - points_range.c.min_points
                ).label('max_diff')
            )
            .select_from(user_points)
            .join(points_range, true())
            .where(
                (user_points.c.total == points_range.c.max_points) |
                (user_points.c.total == points_range.c.min_points)
            )
        )
        result = await self.session.execute(stmt)
        return self._get_points_diff_user(result)

    async def get_users_with_min_points_diff(
            self
    ) -> Iterator[tuple[UserId, str, int, int]] | None:
        """
        Получение пользователей с минимальной разностью очков достижений

        WITH user_points AS (
            SELECT
                u.id AS user_id,
                u.name AS user_name,
                COALESCE(SUM(a.number_points), 0) AS total
            FROM
                users AS u
            JOIN
                users_achievements AS ua ON u.id = ua.user_id
            JOIN
                achievements AS a ON a.id = ua.achievement_id
            GROUP BY
                u.id,
                u.name
        ),
        points_diff AS (
            SELECT
                up1.user_id AS user_id_1,
                up2.user_id AS user_id_2,
                ABS(up1.total - up2.total) AS points_diff
            FROM
                user_points AS up1
            JOIN
                user_points AS up2 ON up1.user_id < up2.user_id
        ),
        min_diff AS (
            SELECT
                MIN(points_diff) AS min_diff
            FROM
                points_diff
        )
        SELECT
            up.user_id,
            up.user_name,
            up.total,
            md.min_diff
        FROM
            user_points AS up
        JOIN
            points_diff AS pd ON up.user_id IN (pd.user_id_1, pd.user_id_2)
        JOIN
            min_diff AS md ON pd.points_diff = md.min_diff
        GROUP BY
            up.user_id, up.user_name, up.total, md.min_diff
        HAVING
            COUNT(
                DISTINCT
                    CASE WHEN
                        up.user_id = pd.user_id_1
                    THEN
                        pd.user_id_2 ELSE pd.user_id_1
                    END
            ) > 0
        """

        # Вычисления на стороне БД
        user_points = self._get_total_points_user()
        points_diff = self._get_points_diff(user_points)
        min_diff = self._get_min_diff(points_diff)

        stmt = (
            select(
                user_points.c.user_id,
                user_points.c.user_name,
                user_points.c.total,
                min_diff.c.min_diff
            )
            .join(
                points_diff,
                (user_points.c.user_id == points_diff.c.user_id_1)
                | (user_points.c.user_id == points_diff.c.user_id_2)
            )
            .join(min_diff, points_diff.c.points_diff == min_diff.c.min_diff)
            .group_by(
                user_points.c.user_id,
                user_points.c.user_name,
                user_points.c.total,
                min_diff.c.min_diff
            )
            .having(
                func.count(
                    case((user_points.c.user_id == points_diff.c.user_id_1,
                          points_diff.c.user_id_2),
                         else_=points_diff.c.user_id_1).distinct()
                ) > 0
            )
        )
        result = await self.session.execute(stmt)
        return self._get_points_diff_user(result)

    def _get_points_diff(self, user_points):
        user_points_2 = user_points.alias('user_points_2')
        return (
            select(
                user_points.c.user_id.label('user_id_1'),
                user_points_2.c.user_id.label('user_id_2'),
                func.abs(
                    user_points.c.total - user_points_2.c.total
                ).label('points_diff')
            )
            .join(
                user_points_2,
                user_points.c.user_id < user_points_2.c.user_id
            )
        ).cte('points_diff')

    def _get_min_diff(self, points_diff):
        return (
            select(
                func.min(points_diff.c.points_diff).label('min_diff')
            )
        ).cte('min_diff')

    def _get_total_points_user(self) -> CTE:
        return (
            select(
                Users.id.label('user_id'),
                Users.name.label('user_name'),
                func.coalesce(
                    func.sum(Achievements.number_points), 0
                ).label('total')
            )
            .join(
                UsersAchievements,
                Users.id == UsersAchievements.user_id
            )
            .join(
                Achievements,
                Achievements.id == UsersAchievements.achievement_id
            )
            .group_by(Users.id, Users.name)
        ).cte('user_points')

    def _get_points_diff_user(
            self,
            result: CursorResult
    ) -> Iterator[tuple[Any]] | None:
        users = result.all()
        if len(users) == 0:
            return None
        return (val.tuple() for val in users)

    def _get_points_range(self, user_points: CTE) -> CTE:
        return (
            select(
                func.max(user_points.c.total).label('max_points'),
                func.min(user_points.c.total).label('min_points')
            )
        ).cte('points_range')

    def _get_max_points_user(self) -> CTE:
        return (
            select(
                Users.id.label('id'),
                Users.name.label('name'),
                func.sum(Achievements.number_points).label('total')
            )
            .join(
                UsersAchievements,
                Users.id == UsersAchievements.user_id
            )
            .join(
                Achievements,
                UsersAchievements.achievement_id == Achievements.id
            )
            .group_by(Users.id, Users.name)
        ).cte('user_points')
