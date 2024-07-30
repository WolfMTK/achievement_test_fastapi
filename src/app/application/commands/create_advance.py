from app.adapter.stubs import StubAchievementGateway
from app.application.dto import CreateAdvanceDTO, AdvanceResultDTO
from app.application.protocols import Interactor, UoW
from app.domain.services import AdvanceService


class CreateAdvance(Interactor[CreateAdvanceDTO, AdvanceResultDTO]):
    def __init__(
            self,
            gateway: StubAchievementGateway,
            uow: UoW,
            service: AdvanceService
    ) -> None:
        self.gateway = gateway
        self.uow = uow
        self.service = service

    async def __call__(self, data: CreateAdvanceDTO) -> AdvanceResultDTO:
        self.service.check_advance(
            await self.gateway.check_advance(name=data.name)
        )
        advance = self.service.create_advance(**data.model_dump())
        advance = await self.gateway.create(
            id=advance.id,
            name=advance.name,
            number_points=str(advance.number_points),
            description=advance.description
        )
        await self.uow.commit()
        return AdvanceResultDTO(id=advance.id)
