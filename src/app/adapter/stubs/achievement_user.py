from abc import ABC, abstractmethod
from collections.abc import Iterator

from app.adapter.sqlalchemy_db.models import UsersAchievements
from app.application.protocols import Created
from app.domain.models import UserId, AchievementId


class StubAchievementUserGateway(
    Created[UsersAchievements],
    ABC
):
    @abstractmethod
    async def get_achievements(
            self,
            user_id: UserId,
            limit: int,
            offset: int
    ) -> Iterator[UsersAchievements]: ...

    @abstractmethod
    async def check_user_id_and_achievement_id(
            self,
            user_id: UserId,
            achievement_id: AchievementId
    ) -> bool: ...

    @abstractmethod
    async def check_achievement_user(
            self,
            user_id: UserId,
            achievement_id: AchievementId
    ) -> bool: ...

    @abstractmethod
    async def get_total_achievements(self, user_id: UserId) -> int: ...

    @abstractmethod
    async def get_max_achievements_user(
            self
    ) -> tuple[UserId, str, int] | None: ...

    @abstractmethod
    async def check_user_exists(self, user_id: UserId) -> bool: ...

    @abstractmethod
    async def get_max_achievement_points_user(
            self
    ) -> tuple[UserId, str, int] | None: ...

    @abstractmethod
    async def get_users_with_max_points_diff(
            self
    ) -> Iterator[tuple[UserId, str, int, int]] | None: ...

    @abstractmethod
    async def get_users_with_min_points_diff(
            self
    ) -> Iterator[tuple[UserId, str, int, int]] | None: ...
