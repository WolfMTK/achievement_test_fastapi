import logging

from fastapi import FastAPI

from app import adapter
from app.core import configure_logging, load_logging_config
from app.presentation.web import user_router, achievement_router
from .di import init_dependencies

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    """ Создать приложение и добавить маршруты. """
    logging_config = load_logging_config()
    configure_logging(logging_config)
    logger.debug('Initialize API')
    app = FastAPI()
    adapter.init_dependency(app)
    init_dependencies(app)
    include_routers(app)
    return app


def include_routers(app: FastAPI):
    """ Включить маршруты. """
    app.include_router(user_router)
    app.include_router(achievement_router)
