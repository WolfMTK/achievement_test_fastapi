from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import Depends

from app.adapter.stubs import StubUserAchievementGateway
from app.application.commands import AddAchievementUser, GetAchievementsUser
from app.application.protocols import UoW
from app.domain.services import AchievementUserService
from app.presentation.interactors import AchievementUserInteractorFactory


class AchievementUserIOC(AchievementUserInteractorFactory):
    def __init__(
            self,
            uow: UoW = Depends(),
            gateway: StubUserAchievementGateway = Depends()
    ) -> None:
        self.uow = uow
        self.gateway = gateway
        self.service = AchievementUserService()

    @asynccontextmanager
    async def add_achievement_user(
            self
    ) -> AsyncIterator[AddAchievementUser]:
        yield AddAchievementUser(
            gateway=self.gateway,
            uow=self.uow,
            service=self.service
        )

    @asynccontextmanager
    async def get_achievement_user(
            self
    ) -> AsyncIterator[GetAchievementsUser]:
        yield GetAchievementsUser(
            gateway=self.gateway,
            service=self.service
        )
