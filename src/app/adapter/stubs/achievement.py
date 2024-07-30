from abc import ABC, abstractmethod
from typing import Any

from app.adapter.sqlalchemy_db.models import Achievements
from app.application.protocols import ReadingAll, Created


class StubAchievementGateway(ReadingAll[Achievements], Created[Achievements], ABC):
    @abstractmethod
    async def get_total_advances(self, *args: Any, **kwargs: Any) -> int: ...

    @abstractmethod
    async def check_advance(self, *args: Any, **kwargs: Any) -> bool: ...
