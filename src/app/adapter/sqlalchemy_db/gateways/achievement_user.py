from sqlalchemy import insert, select, ScalarResult
from sqlalchemy.sql import func

from app.adapter.sqlalchemy_db.models import UsersAchievements, Users, Achievements
from app.adapter.stubs.achievement_user import StubUserAdvanceGateway
from app.domain.models import UserId, AdvanceId
from .base import BaseGateway


class UserAdvanceGateway(BaseGateway, StubUserAdvanceGateway):
    async def get_advances(
            self,
            user_id: UserId,
            limit: int,
            offset: int
    ) -> ScalarResult[UsersAchievements]:
        """
        Получение достижений пользователя.

        Пример запроса:

        SELECT
            ua.user_id,
            ua.advance_id,
            ua.date_one
        FROM
            users_advances AS ua
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
            advance_id: AdvanceId
    ) -> UsersAchievements:
        """
        Добавить достижения пользователю

        Пример запроса:

        INSERT INTO
            users_advances (user_id, advance_id)
        VALUES
            ($1, $2)
        """
        stmt = insert(UsersAchievements).values(
            user_id=user_id,
            advance_id=advance_id,
        ).returning(UsersAchievements)
        result = await self.session.execute(stmt)
        return result.scalar()

    async def check_user_id_and_advance_id(
            self,
            user_id: UserId,
            advance_id: AdvanceId
    ) -> bool:
        """
        Проверить user_id и advance_id.

        Пример запроса:
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
                advances AS a ON u.id = $1 AND a.id = $2
        )
        """
        stmt = select(Users, Achievements).join(
            Achievements,
            (Users.id == user_id) & (Achievements.id == advance_id)
        ).exists()
        return await self.session.scalar(select(stmt))

    async def check_advance_user(
            self,
            user_id: UserId,
            advance_id: AdvanceId
    ) -> bool:
        """
        Проверка наличия достижения у пользователя.

        SELECT
            ua.user_id,
            ua.advance_id,
            us.date_on
        FROM
            users_advances
        WHERE
            ua.user_id = $1 AND ua.advance_id = $2
        """
        stmt = select(UsersAchievements).where(
            UsersAchievements.user_id == user_id,
            UsersAchievements.advance_id == advance_id
        ).exists()
        return await self.session.scalar(select(stmt))

    async def get_total_advances(self, user_id: UserId) -> int:
        """
        Получить количество достижений пользователя.

        SELECT
            COUNT(ua.advance_id)
        FROM
            users_advances AS ua
        WHERE
            us.user_id = $1
        """
        stmt = select(func.count(UsersAchievements.advance_id)).where(
            UsersAchievements.user_id == user_id
        )
        return await self.session.scalar(stmt)
