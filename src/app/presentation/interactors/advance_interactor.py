from abc import ABC, abstractmethod
from contextlib import AbstractAsyncContextManager

from app.application.commands import CreateAdvance, GetAdvances


class AdvanceInteractorFactory(ABC):
    @abstractmethod
    def create_advance(
            self
    ) -> AbstractAsyncContextManager[CreateAdvance]: ...

    @abstractmethod
    def get_advances(self) -> AbstractAsyncContextManager[GetAdvances]: ...
