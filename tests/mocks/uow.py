from app.application.protocols import UoW


class UoWMock(UoW):
    def __init__(self) -> None:
        self.commited = False
        self.rolled_back = False
        self.flushing = False

    async def commit(self) -> None:
        if self.rolled_back:
            raise ValueError('Cannot commit after rolling back')
        if self.flushing:
            raise ValueError('Cannot commit after flushing')
        self.commited = True

    async def rollback(self) -> None:
        if self.commited:
            raise ValueError('Cannot rollback after commiting')
        if self.flushing:
            raise ValueError('Cannot rollback after flushing')
        self.rolled_back = True

    async def flush(self) -> None:
        if self.commited:
            raise ValueError('Cannot flush after commiting')
        if self.rolled_back:
            raise ValueError('Cannot flush after rolling back')
        self.flushing = True
