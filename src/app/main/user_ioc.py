from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import Depends

from app.adapter.stubs import StubUserGateway
from app.application.commands import GetUserInfo
from app.application.protocols import UoW
from app.domain.services import UserService
from app.presentation.interactors import UserInteractorFactory


class UserIOC(UserInteractorFactory):
    def __init__(
            self,
            uow: UoW = Depends(),
            gateway: StubUserGateway = Depends()
    ) -> None:
        self.uow = uow
        self.gateway = gateway
        self.service = UserService()

    @asynccontextmanager
    async def get_user_info(self) -> AsyncIterator[GetUserInfo]:
        yield GetUserInfo(
            service=self.service,
            gateway=self.gateway
        )
