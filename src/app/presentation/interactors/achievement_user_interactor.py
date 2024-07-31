from abc import ABC, abstractmethod
from contextlib import AbstractAsyncContextManager

from app.application.commands import (
    AddAchievementUser,
    GetAchievementsUser,
    GetMaxAchievementsUser,
    GetMaxAchievementPointsUser
)


class AchievementUserInteractorFactory(ABC):
    @abstractmethod
    def add_achievement_user(
            self
    ) -> AbstractAsyncContextManager[AddAchievementUser]: ...

    @abstractmethod
    def get_achievement_user(
            self
    ) -> AbstractAsyncContextManager[GetAchievementsUser]: ...

    @abstractmethod
    def get_max_achievements_user(
            self
    ) -> AbstractAsyncContextManager[GetMaxAchievementsUser]: ...

    @abstractmethod
    def get_max_achievement_points_user(
            self
    ) -> AbstractAsyncContextManager[GetMaxAchievementPointsUser]: ...
