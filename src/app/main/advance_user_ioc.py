from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import Depends

from app.adapter.stubs import StubUserAdvanceGateway
from app.application.commands import AddAdvanceUser, GetAdvanceUser
from app.application.protocols import UoW
from app.domain.services import AdvanceUserService
from app.presentation.interactors import AdvanceUserInteractorFactory


class AdvanceUserIOC(AdvanceUserInteractorFactory):
    def __init__(
            self,
            uow: UoW = Depends(),
            gateway: StubUserAdvanceGateway = Depends()
    ) -> None:
        self.uow = uow
        self.gateway = gateway
        self.service = AdvanceUserService()

    @asynccontextmanager
    async def add_advance_user(
            self
    ) -> AsyncIterator[AddAdvanceUser]:
        yield AddAdvanceUser(
            gateway=self.gateway,
            uow=self.uow,
            service=self.service
        )

    @asynccontextmanager
    async def get_advance_user(
            self
    ) -> AsyncIterator[GetAdvanceUser]:
        yield GetAdvanceUser(
            gateway=self.gateway,
            service=self.service
        )
