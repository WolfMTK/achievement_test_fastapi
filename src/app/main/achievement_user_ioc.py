from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import Depends

from app.adapter.stubs import StubAchievementUserGateway
from app.application.commands import (
    AddAchievementUser,
    GetAchievementsUser,
    GetMaxAchievementsUser,
    GetMaxAchievementPointsUser,
    GetUsersWithMaxPointsDiff
)
from app.application.protocols import UoW
from app.domain.services import AchievementUserService
from app.presentation.interactors import AchievementUserInteractorFactory


class AchievementUserIOC(AchievementUserInteractorFactory):
    def __init__(
            self,
            uow: UoW = Depends(),
            gateway: StubAchievementUserGateway = Depends()
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

    @asynccontextmanager
    async def get_max_achievements_user(
            self
    ) -> AsyncIterator[GetMaxAchievementsUser]:
        yield GetMaxAchievementsUser(
            gateway=self.gateway,
            service=self.service
        )

    @asynccontextmanager
    async def get_max_achievement_points_user(
            self
    ) -> AsyncIterator[GetMaxAchievementPointsUser]:
        yield GetMaxAchievementPointsUser(
            gateway=self.gateway,
            service=self.service
        )

    @asynccontextmanager
    async def get_users_with_max_points_diff(
            self
    ) -> AsyncIterator[GetUsersWithMaxPointsDiff]:
        yield GetUsersWithMaxPointsDiff(
            gateway=self.gateway,
            service=self.service
        )
