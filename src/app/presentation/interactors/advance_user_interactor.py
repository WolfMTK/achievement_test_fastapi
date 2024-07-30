from abc import ABC, abstractmethod
from contextlib import AbstractAsyncContextManager

from app.application.commands import AddAdvanceUser, GetAdvanceUser


class AdvanceUserInteractorFactory(ABC):
    @abstractmethod
    def add_advance_user(
            self
    ) -> AbstractAsyncContextManager[AddAdvanceUser]: ...

    @abstractmethod
    def get_advance_user(
            self
    ) -> AbstractAsyncContextManager[GetAdvanceUser]: ...

