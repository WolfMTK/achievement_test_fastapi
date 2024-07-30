from app.adapter.stubs import StubUserAdvanceGateway
from app.application.dto import GetAdvanceUserDTO, AdvanceUserListDTO
from app.application.protocols import Interactor
from app.domain.services import AdvanceUserService


class GetAdvanceUser(Interactor[GetAdvanceUserDTO, AdvanceUserListDTO]):
    def __init__(
            self,
            gateway: StubUserAdvanceGateway,
            service: AdvanceUserService
    ) -> None:
        self.gateway = gateway
        self.service = service

    async def __call__(self, data: GetAdvanceUserDTO) -> AdvanceUserListDTO:
        limit = data.pagination.limit
        offset = data.pagination.offset * limit
        advance_user = await self.gateway.get_advances(
            user_id=data.user_id,
            limit=limit,
            offset=offset
        )
        total = await self.gateway.get_total_advances(user_id=data.user_id)
        return AdvanceUserListDTO(
            total=total,
            limit=data.pagination.limit,
            offset=data.pagination.offset,
            user_id=data.user_id,
            advances=self.service.get_advances(advance_user)
        )
