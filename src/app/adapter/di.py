import functools
from collections.abc import Iterator

from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapter.sqlalchemy_db import (
    create_async_session_maker,
    create_async_session,
)
from app.adapter.sqlalchemy_db.gateways import (
    UserGateway,
    AchievementGateway,
    UserAchievementGateway,
)
from app.adapter.stubs import (
    StubUserGateway,
    StubAchievementGateway,
    StubUserAchievementGateway,
)
from app.application.protocols import UoW
from app.core import Stub, load_database_config


def new_uow(
        session: AsyncSession = Depends(Stub(AsyncSession))
) -> AsyncSession:
    return session


def new_user_gateway(
        session: AsyncSession = Depends(Stub(AsyncSession))
) -> Iterator[UserGateway]:
    yield UserGateway(session)


def new_achievement_gateway(
        session: AsyncSession = Depends(Stub(AsyncSession))
) -> Iterator[AchievementGateway]:
    yield AchievementGateway(session)


def new_user_achievement_gateway(
        session: AsyncSession = Depends(Stub(AsyncSession))
) -> Iterator[UserAchievementGateway]:
    yield UserAchievementGateway(session)


def init_dependency(app: FastAPI) -> None:
    """ Инициализировать зависимости. """
    db_url = load_database_config().db_url
    session_maker = create_async_session_maker(db_url)

    app.dependency_overrides.update(
        {
            AsyncSession: functools.partial(create_async_session, session_maker),
            UoW: new_uow,
            StubUserGateway: new_user_gateway,
            StubAchievementGateway: new_achievement_gateway,
            StubUserAchievementGateway: new_user_achievement_gateway
        }
    )
