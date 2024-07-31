from typing import Any

from app.adapter.stubs import StubAchievementUserGateway
from app.application.dto import MaxAchievementPointsUserResultDTO
from app.application.protocols import Interactor
from app.domain.services import AchievementUserService


class GetMaxAchievementPointsUser(
    Interactor[None, MaxAchievementPointsUserResultDTO]
):
    def __init__(
            self,
            gateway: StubAchievementUserGateway,
            service: AchievementUserService
    ) -> None:
        self.gateway = gateway
        self.service = service

    async def __call__(self, **kwargs: Any) -> MaxAchievementPointsUserResultDTO:
        data = await self.gateway.get_max_achievement_points_user()
        self.service.check_max_points_user(data)
        user_id, name, total = data
        return MaxAchievementPointsUserResultDTO(
            id=user_id,
            name=name,
            total_points=total
        )
