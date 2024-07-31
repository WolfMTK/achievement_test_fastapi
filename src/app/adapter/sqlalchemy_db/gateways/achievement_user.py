from sqlalchemy import insert, select, ScalarResult, desc
from sqlalchemy.sql import func

from app.adapter.sqlalchemy_db.models import (
    UsersAchievements,
    Users,
    Achievements
)
from app.adapter.stubs.achievement_user import StubUserAchievementGateway
from app.domain.models import UserId, AchievementId
from .base import BaseGateway

LIMIT = 1


class UserAchievementGateway(BaseGateway, StubUserAchievementGateway):
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
            u.id, u.name
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
