from abc import ABC, abstractmethod
from contextlib import AbstractAsyncContextManager

from app.application.commands import GetUserInfo


class UserInteractorFactory(ABC):
    """ Фабрика интеракторов (или абстрактная фабрика) """

    @abstractmethod
    def get_user_info(self) -> AbstractAsyncContextManager[GetUserInfo]: ...
