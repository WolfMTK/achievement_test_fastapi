from abc import ABC, abstractmethod
from contextlib import AbstractAsyncContextManager

from app.application.commands import CreateAchievement, GetAchievements


class AchievementInteractorFactory(ABC):
    @abstractmethod
    def create_achievement(
            self
    ) -> AbstractAsyncContextManager[CreateAchievement]: ...

    @abstractmethod
    def get_achievements(self) -> AbstractAsyncContextManager[GetAchievements]: ...
