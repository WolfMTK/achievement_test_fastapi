import logging

from app.adapter.stubs import StubAchievementUserGateway
from app.application.dto import GetAchievementUserDTO, AchievementUserListDTO
from app.application.protocols import Interactor
from app.domain.services import AchievementUserService

logger = logging.getLogger(__name__)


class GetAchievementsUser(Interactor[GetAchievementUserDTO, AchievementUserListDTO]):
    def __init__(
            self,
            gateway: StubAchievementUserGateway,
            service: AchievementUserService
    ) -> None:
        self.gateway = gateway
        self.service = service

    async def __call__(self, data: GetAchievementUserDTO) -> AchievementUserListDTO:
        self.service.check_user(
            await self.gateway.check_user_exists(data.user_id)
        )
        limit = data.pagination.limit
        offset = data.pagination.offset * limit
        achievement_user = await self.gateway.get_achievements(
            user_id=data.user_id,
            limit=limit,
            offset=offset
        )
        total = await self.gateway.get_total_achievements(user_id=data.user_id)
        logger.debug(f'Get achievements the user {data.user_id}')
        return AchievementUserListDTO(
            total=total,
            limit=data.pagination.limit,
            offset=data.pagination.offset,
            user_id=data.user_id,
            achievements=self.service.get_achievement(achievement_user)
        )
