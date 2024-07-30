from typing import Any

from sqlalchemy import select

from app.adapter.sqlalchemy_db.models import Users
from app.adapter.stubs import StubUserGateway
from .base import BaseGateway


class UserGateway(BaseGateway, StubUserGateway):
    async def get(self, **kwargs: Any) -> Users | None:
        """
        Получить данные пользователя.

        Пример выполняемого запроса:
        SELECT
            u.id,
            u.name,
            u.language
        FROM
            users AS u
        WHERE
            u.id = $1
        """
        stmt = select(Users).filter_by(**kwargs)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
