from abc import ABC, abstractmethod
from contextlib import AbstractAsyncContextManager

from app.application.commands import AddAchievementUser, GetAchievementsUser


class AchievementUserInteractorFactory(ABC):
    @abstractmethod
    def add_achievement_user(
            self
    ) -> AbstractAsyncContextManager[AddAchievementUser]: ...

    @abstractmethod
    def get_achievement_user(
            self
    ) -> AbstractAsyncContextManager[GetAchievementsUser]: ...

