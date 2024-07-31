from typing import Any

from app.adapter.stubs import StubAchievementUserGateway
from app.application.dto import UserWithMinPointsDiffResultDTO
from app.application.protocols import Interactor
from app.domain.services import AchievementUserService


class GetUsersWithMinPointsDiff(
    Interactor[None, list[UserWithMinPointsDiffResultDTO]]
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
    ) -> list[UserWithMinPointsDiffResultDTO]:
        data = await self.gateway.get_users_with_min_points_diff()
        self.service.check_min_points_diff_users(data)
        return [UserWithMinPointsDiffResultDTO(
            id=user_id,
            name=name,
            total_points=total,
            min_diff=min_diff
        ) for user_id, name, total, min_diff in data]
