from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import Depends

from app.adapter.stubs import StubAchievementGateway
from app.application.commands.create_achievement import CreateAchievement
from app.application.commands.get_achievements import GetAchievements
from app.application.protocols import UoW
from app.domain.services import AchievementService
from app.presentation.interactors import AchievementInteractorFactory


class AchievementIOC(AchievementInteractorFactory):
    def __init__(
            self,
            uow: UoW = Depends(),
            gateway: StubAchievementGateway = Depends()
    ) -> None:
        self.uow = uow
        self.gateway = gateway
        self.service = AchievementService()

    @asynccontextmanager
    async def create_achievement(
            self
    ) -> AsyncIterator[CreateAchievement]:
        yield CreateAchievement(
            gateway=self.gateway,
            uow=self.uow,
            service=self.service
        )

    @asynccontextmanager
    async def get_achievements(self) -> AsyncIterator[GetAchievements]:
        yield GetAchievements(
            gateway=self.gateway,
            service=self.service
        )
