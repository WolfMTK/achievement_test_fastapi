from fastapi import FastAPI

from app import adapter


def create_app() -> FastAPI:
    """ Создать приложение и добавить маршруты. """
    app = FastAPI()
    adapter.init_dependency(app)
    return app
