from fastapi import FastAPI


def create_app() -> FastAPI:
    """ Создать приложение и добавить маршруты. """
    app = FastAPI()
    return app
