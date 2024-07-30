from app.adapter.stubs import StubUserAdvanceGateway
from app.application.dto.advance_user import (
    NewAdvanceUserDTO,
    AdvanceUserResultDTO
)
from app.application.protocols import Interactor, UoW
from app.domain.services import AdvanceUserService


class AddAdvanceUser(Interactor[NewAdvanceUserDTO, AdvanceUserResultDTO]):
    def __init__(
            self,
            gateway: StubUserAdvanceGateway,
            uow: UoW,
            service: AdvanceUserService
    ) -> None:
        self.gateway = gateway
        self.uow = uow
        self.service = service

    async def __call__(self, data: NewAdvanceUserDTO) -> AdvanceUserResultDTO:
        self.service.check_advance_and_user(
            await self.gateway.check_user_id_and_advance_id(**data.model_dump())
        )
        self.service.check_advance_user(
            await self.gateway.check_advance_user(**data.model_dump())
        )
        advance_user = await self.gateway.create(**data.model_dump())
        await self.uow.commit()
        return AdvanceUserResultDTO(
            user_id=advance_user.user_id,
            advance_id=advance_user.advance_id,
            date_on=advance_user.date_on
        )
