import logging
from typing import Any

from app.adapter.stubs import StubAchievementUserGateway
from app.application.dto import UserInfoDTO
from app.application.protocols import Interactor

logger = logging.getLogger(__name__)


class GetUsersWithDaysStreak(
    Interactor[None, list[UserInfoDTO]]
):
    def __init__(
            self,
            gateway: StubAchievementUserGateway,
    ) -> None:
        self.gateway = gateway

    async def __call__(
            self,
            **kwargs: Any
    ) -> list[UserInfoDTO]:
        users = await self.gateway.get_users_with_days_streak()
        logging.debug('Get users with days streak')
        return [UserInfoDTO(
            id=user.id,
            name=user.name,
            language=user.language
        ) for user in users]
