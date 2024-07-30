from abc import ABC, abstractmethod
from collections.abc import Iterator

from app.adapter.sqlalchemy_db.models import UsersAchievements
from app.application.protocols import Created
from app.domain.models import UserId, AdvanceId


class StubUserAdvanceGateway(
    Created[UsersAchievements],
    ABC
):
    @abstractmethod
    async def get_advances(
            self,
            user_id: UserId,
            limit: int,
            offset: int
    ) -> Iterator[UsersAchievements]: ...

    @abstractmethod
    async def check_user_id_and_advance_id(
            self,
            user_id: UserId,
            advance_id: AdvanceId
    ) -> bool: ...

    @abstractmethod
    async def check_advance_user(
            self,
            user_id: UserId,
            advance_id: AdvanceId
    ) -> bool: ...

    @abstractmethod
    async def get_total_advances(self, user_id: UserId) -> int: ...
