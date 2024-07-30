from app.adapter.stubs import StubUserAchievementGateway
from app.application.dto.achievement_user import (
    NewAchievementUserDTO,
    AchievementUserResultDTO
)
from app.application.protocols import Interactor, UoW
from app.domain.services import AchievementUserService


class AddAchievementUser(
    Interactor[NewAchievementUserDTO, AchievementUserResultDTO]
):
    def __init__(
            self,
            gateway: StubUserAchievementGateway,
            uow: UoW,
            service: AchievementUserService
    ) -> None:
        self.gateway = gateway
        self.uow = uow
        self.service = service

    async def __call__(
            self,
            data: NewAchievementUserDTO
    ) -> AchievementUserResultDTO:
        self.service.check_achievement_and_user(
            await self.gateway.check_user_id_and_achievement_id(
                **data.model_dump()
            )
        )
        self.service.check_achievement_user(
            await self.gateway.check_achievement_user(**data.model_dump())
        )
        achievement_user = await self.gateway.create(**data.model_dump())
        await self.uow.commit()
        return AchievementUserResultDTO(
            user_id=achievement_user.user_id,
            achievement_id=achievement_user.achievement_id,
            date_on=self.service.get_date_on(achievement_user.date_on)
        )
