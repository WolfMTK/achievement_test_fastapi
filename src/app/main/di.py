from fastapi import FastAPI

from app.main.user_ioc import UserIOC
from app.presentation.interactors import UserInteractorFactory


def init_dependencies(app: FastAPI) -> None:
    """ Инициализировать зависимости. """
    app.dependency_overrides.update({
        UserInteractorFactory: UserIOC
    })
