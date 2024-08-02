import pytest

from app.application.commands import CreateAchievement
from app.application.dto import CreateAchievementDTO
from app.domain.exceptions import AchievementExistsException
from app.domain.services import AchievementService
from tests.mocks.achievement import AchievementGatewayMock
from tests.mocks.uow import UoWMock


async def test_create_achievement(
        achievement_gateway: AchievementGatewayMock,
        uow: UoWMock
) -> None:
    gateway = achievement_gateway
    handler = CreateAchievement(
        gateway=gateway,
        uow=uow,
        service=AchievementService()
    )
    data = CreateAchievementDTO(
        name='test | тест',
        number_points=10,
        description='test | тест'
    )
    data = await handler(data)
    assert data.id == gateway.user_uuid
    assert uow.commited is True
    assert uow.flushing is False
    assert uow.rolled_back is False


async def test_create_achievement_invalid(
        achievement_gateway: AchievementGatewayMock,
        uow: UoWMock
) -> None:
    gateway = achievement_gateway
    gateway.is_check = True
    handler = CreateAchievement(
        gateway=gateway,
        uow=uow,
        service=AchievementService()
    )
    data = CreateAchievementDTO(
        name='test | тест',
        number_points=10,
        description='test | тест'
    )
    with pytest.raises(AchievementExistsException):
        await handler(data)

    assert uow.commited is False
    assert uow.flushing is False
    assert uow.rolled_back is False
