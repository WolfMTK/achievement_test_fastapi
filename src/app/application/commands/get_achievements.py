from app.adapter.stubs import StubAchievementGateway
from app.application.dto import GetAchievementListDTO, AchievementListDTO
from app.application.protocols import Interactor
from app.domain.services import AchievementService


class GetAchievements(Interactor[GetAchievementListDTO, AchievementListDTO]):
    def __init__(
            self,
            gateway: StubAchievementGateway,
            service: AchievementService
    ) -> None:
        self.gateway = gateway
        self.service = service

    async def __call__(self, data: GetAchievementListDTO) -> AchievementListDTO:
        limit = data.pagination.limit
        offset = data.pagination.offset * limit
        achievements = await self.gateway.get_all(limit=limit, offset=offset)
        total = await self.gateway.get_total_achievements()
        achievements = self.service.get_achievements(achievements)
        return AchievementListDTO(
            total=total,
            limit=data.pagination.limit,
            offset=data.pagination.offset,
            achievements=achievements
        )
