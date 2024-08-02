from abc import ABC, abstractmethod
from collections.abc import Iterator
from typing import Any


class Created[T](ABC):
    @abstractmethod
    async def create(self, *args: Any, **kwargs: Any) -> T: ...


class Reading[T](ABC):
    @abstractmethod
    async def get(self, *args: Any, **kwargs: Any) -> T | None: ...


class ReadingAll[T](ABC):
    @abstractmethod
    async def get_all(self, *args: Any, **kwargs: Any) -> Iterator[T]: ...


class Updating[T](ABC):
    @abstractmethod
    async def update(self, *args: Any, **kwargs: Any) -> T: ...


class Deleted[T](ABC):
    @abstractmethod
    async def delete(self, *args: Any, **kwargs: Any) -> T: ...
