from app.adapter.stubs import StubAchievementGateway
from app.application.dto import GetAdvanceListDTO, AdvanceListDTO
from app.application.protocols import Interactor
from app.domain.services import AdvanceService


class GetAdvances(Interactor[GetAdvanceListDTO, AdvanceListDTO]):
    def __init__(
            self,
            gateway: StubAchievementGateway,
            service: AdvanceService
    ) -> None:
        self.gateway = gateway
        self.service = service

    async def __call__(self, data: GetAdvanceListDTO) -> AdvanceListDTO:
        limit = data.pagination.limit
        offset = data.pagination.offset * limit
        advances = await self.gateway.get_all(limit=limit, offset=offset)
        total = await self.gateway.get_total_advances()
        advances = self.service.get_advances(advances)
        return AdvanceListDTO(
            total=total,
            limit=data.pagination.limit,
            offset=data.pagination.offset,
            advances=advances
        )
