from typing import Any

from sqlalchemy import select, insert, ScalarResult
from sqlalchemy.sql import func

from app.adapter.sqlalchemy_db.models import Achievements
from app.adapter.stubs.advance import StubAchievementGateway
from .base import BaseGateway


class AchievementGateway(BaseGateway, StubAchievementGateway):
    async def create(self, *args: Any, **kwargs: Any) -> Achievements:
        """
        Создать достижение.

        Пример запроса:
        INSERT INTO
            achievements (id, name, number_points, description)
        VALUES
            ($1, $2, $3, $4)
        """
        stmt = insert(Achievements).values(**kwargs).returning(Achievements)
        result = await self.session.execute(stmt)
        return result.scalar()

    async def get_all(self, limit: int, offset: int) -> ScalarResult[Achievements]:
        """
        Получить все достижения.

        Пример запроса:
        SELECT
            a.id
            a.name,
            a.number_points,
            a.description
        FROM
            advances AS a
        LIMIT
            $1
        OFFSET
            $2
        """
        stmt = select(Achievements).limit(limit).offset(offset)
        result = await self.session.execute(stmt)
        return result.scalars()

    async def get_total_advances(self) -> int:
        """
        Получить количество достижений.

        Пример запроса:
        SELECT
            COUNT(a.id)
        FROM
            advances AS a
        """
        stmt = select(func.count(Achievements.id))
        return await self.session.scalar(stmt)

    async def check_advance(self, **kwargs: Any) -> bool:
        """
        Проверить наличия записи о достижении.

        Пример запроса:
        SELECT EXISTS
            (SELECT
                a.id,
                a.name,
                a.number_points,
                a.description
             FROM
                advances AS a
             WHERE
                a.name = $1)
        """

        stmt = select(Achievements).filter_by(**kwargs).exists()
        return await self.session.scalar(select(stmt))
