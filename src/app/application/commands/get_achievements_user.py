from app.adapter.stubs import StubUserAchievementGateway
from app.application.dto import GetAchievementUserDTO, AchievementUserListDTO
from app.application.protocols import Interactor
from app.domain.services import AchievementUserService


class GetAchievementsUser(Interactor[GetAchievementUserDTO, AchievementUserListDTO]):
    def __init__(
            self,
            gateway: StubUserAchievementGateway,
            service: AchievementUserService
    ) -> None:
        self.gateway = gateway
        self.service = service

    async def __call__(self, data: GetAchievementUserDTO) -> AchievementUserListDTO:
        limit = data.pagination.limit
        offset = data.pagination.offset * limit
        achievement_user = await self.gateway.get_achievements(
            user_id=data.user_id,
            limit=limit,
            offset=offset
        )
        total = await self.gateway.get_total_achievements(user_id=data.user_id)
        return AchievementUserListDTO(
            total=total,
            limit=data.pagination.limit,
            offset=data.pagination.offset,
            user_id=data.user_id,
            achievements=self.service.get_achievement(achievement_user)
        )
