from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


def create_async_session_maker(
        db_url: str
) -> async_sessionmaker[AsyncSession]:
    """ Создание sessionmaker для генерации асинхронной сессии. """
    engine = create_async_engine(db_url)
    return async_sessionmaker(engine, expire_on_commit=False)


async def create_async_session(
        session_maker: async_sessionmaker
) -> AsyncIterator[AsyncSession]:
    """ Создать асинхронную сессию. """
    async with session_maker() as session:
        yield session
