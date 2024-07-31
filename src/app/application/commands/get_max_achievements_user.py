from typing import Any

from app.adapter.stubs import StubUserAchievementGateway
from app.application.dto import MaxAchievementsUserResultDTO
from app.application.protocols import Interactor
from app.domain.services import AchievementUserService


class GetMaxAchievementsUser(Interactor[None, MaxAchievementsUserResultDTO]):
    def __init__(
            self,
            gateway: StubUserAchievementGateway,
            service: AchievementUserService
    ) -> None:
        self.gateway = gateway
        self.service = service

    async def __call__(self, **kwargs: Any) -> MaxAchievementsUserResultDTO:
        data = await self.gateway.get_max_achievements_user()
        self.service.check_max_achievements_user(data)
        user_id, name, count = data
        return MaxAchievementsUserResultDTO(
            id=user_id,
            name=name,
            count=count
        )
