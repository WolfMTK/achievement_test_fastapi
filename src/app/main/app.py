from fastapi import FastAPI

from app import adapter
from .di import init_dependencies
from app.presentation.web import user_router


def create_app() -> FastAPI:
    """ Создать приложение и добавить маршруты. """
    app = FastAPI()
    adapter.init_dependency(app)
    init_dependencies(app)
    include_routers(app)
    return app


def include_routers(app: FastAPI):
    """ Включить маршруты. """
    app.include_router(user_router)
