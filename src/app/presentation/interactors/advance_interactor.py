from abc import ABC, abstractmethod
from contextlib import AbstractAsyncContextManager

from app.application.commands.create_advance import CreateAdvance


class AdvanceInteractorFactory(ABC):
    @abstractmethod
    def create_advance(
            self
    ) -> AbstractAsyncContextManager[CreateAdvance]: ...
