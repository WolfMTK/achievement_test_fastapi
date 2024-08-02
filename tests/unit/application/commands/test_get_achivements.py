from app.application.commands import GetAchievements
from app.application.dto import GetAchievementListDTO, Pagination
from app.domain.services import AchievementService
from tests.mocks.achievement import AchievementGatewayMock


async def test_get_achievements(
        achievement_gateway: AchievementGatewayMock,
) -> None:
    gateway = achievement_gateway
    handler = GetAchievements(
        gateway=gateway,
        service=AchievementService()
    )
    limit = 10
    offset = 0
    data = GetAchievementListDTO(
        Pagination(
            limit=limit,
            offset=offset
        )
    )
    data = await handler(data)
    assert limit == data.limit
    assert offset == data.offset
    assert gateway.total == data.total
    assert len(data.achievements) == data.total
