from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapter.sqlalchemy_db import (
    create_async_session_maker,
    create_async_session,
)
from app.application.protocols import UoW
from app.core import Stub, load_database_config


def new_uow(
        session: AsyncSession = Depends(Stub(AsyncSession))
) -> AsyncSession:
    return session


def init_dependency(app: FastAPI) -> None:
    db_url = load_database_config().db_url
    session_maker = create_async_session_maker(db_url)

    app.dependency_overrides.update(
        {
            AsyncSession: lambda: create_async_session(session_maker),
            UoW: new_uow
        }
    )
