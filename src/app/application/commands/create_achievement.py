from app.adapter.stubs import StubAchievementGateway
from app.application.dto import CreateAchievementDTO, AchievementResultDTO
from app.application.protocols import Interactor, UoW
from app.domain.services import AchievementService


class CreateAchievement(Interactor[CreateAchievementDTO, AchievementResultDTO]):
    def __init__(
            self,
            gateway: StubAchievementGateway,
            uow: UoW,
            service: AchievementService
    ) -> None:
        self.gateway = gateway
        self.uow = uow
        self.service = service

    async def __call__(self, data: CreateAchievementDTO) -> AchievementResultDTO:
        self.service.check_achievement(
            await self.gateway.check_achievement(name=data.name)
        )
        achievement = self.service.create_achievement(**data.model_dump())
        achievement = await self.gateway.create(
            id=achievement.id,
            name=achievement.name,
            number_points=achievement.number_points,
            description=achievement.description
        )
        await self.uow.commit()
        return AchievementResultDTO(id=achievement.id)
