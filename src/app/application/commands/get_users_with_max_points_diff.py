import logging
from typing import Any

from app.adapter.stubs import StubAchievementUserGateway
from app.application.dto import UserWithMaxPointsDiffResultDTO
from app.application.protocols import Interactor
from app.domain.services import AchievementUserService

logger = logging.getLogger(__name__)


class GetUsersWithMaxPointsDiff(
    Interactor[None, list[UserWithMaxPointsDiffResultDTO]]
):
    def __init__(
            self,
            gateway: StubAchievementUserGateway,
            service: AchievementUserService
    ) -> None:
        self.gateway = gateway
        self.service = service

    async def __call__(
            self,
            **kwargs: Any
    ) -> list[UserWithMaxPointsDiffResultDTO]:
        data = await self.gateway.get_users_with_max_points_diff()
        self.service.check_max_points_diff_users(data)
        logger.debug('Get users with max points diff')
        return [UserWithMaxPointsDiffResultDTO(
            id=user_id,
            name=name,
            total_points=total,
            max_diff=max_diff
        ) for user_id, name, total, max_diff in data]
