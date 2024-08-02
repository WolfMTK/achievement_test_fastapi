from fastapi import FastAPI

from app.presentation.interactors import (
    UserInteractorFactory,
    AchievementInteractorFactory,
    AchievementUserInteractorFactory
)
from .achievement_ioc import AchievementIOC
from .achievement_user_ioc import AchievementUserIOC
from .user_ioc import UserIOC


def init_dependencies(app: FastAPI) -> None:
    """ Инициализировать зависимости. """
    app.dependency_overrides.update({
        UserInteractorFactory: UserIOC,
        AchievementInteractorFactory: AchievementIOC,
        AchievementUserInteractorFactory: AchievementUserIOC
    })
