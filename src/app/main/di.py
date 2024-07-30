from fastapi import FastAPI

from app.presentation.interactors import (
    UserInteractorFactory,
    AdvanceInteractorFactory,
    AdvanceUserInteractorFactory
)
from .advance_ioc import AdvanceIOC
from .advance_user_ioc import AdvanceUserIOC
from .user_ioc import UserIOC


def init_dependencies(app: FastAPI) -> None:
    """ Инициализировать зависимости. """
    app.dependency_overrides.update({
        UserInteractorFactory: UserIOC,
        AdvanceInteractorFactory: AdvanceIOC,
        AdvanceUserInteractorFactory: AdvanceUserIOC
    })
