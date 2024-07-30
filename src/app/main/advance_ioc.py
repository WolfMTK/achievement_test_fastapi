from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import Depends

from app.adapter.stubs import StubAchievementGateway
from app.application.commands.create_advance import CreateAdvance
from app.application.commands.get_advances import GetAdvances
from app.application.protocols import UoW
from app.domain.services import AdvanceService
from app.presentation.interactors import AdvanceInteractorFactory


class AdvanceIOC(AdvanceInteractorFactory):
    def __init__(
            self,
            uow: UoW = Depends(),
            gateway: StubAchievementGateway = Depends()
    ) -> None:
        self.uow = uow
        self.gateway = gateway
        self.service = AdvanceService()

    @asynccontextmanager
    async def create_advance(
            self
    ) -> AsyncIterator[CreateAdvance]:
        yield CreateAdvance(
            gateway=self.gateway,
            uow=self.uow,
            service=self.service
        )

    @asynccontextmanager
    async def get_advances(self) -> AsyncIterator[GetAdvances]:
        yield GetAdvances(
            gateway=self.gateway,
            service=self.service
        )
