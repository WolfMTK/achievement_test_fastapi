import pytest

from app.application.commands import GetMaxAchievementsUser
from app.domain.exceptions import MaxAchievementsNotFound
from app.domain.services import AchievementUserService
from tests.mocks.achievement_users import AchievementUserGatewayMock


async def test_get_max_achievements_user(
        achievement_users_gateway: AchievementUserGatewayMock
) -> None:
    gateway = achievement_users_gateway
    handler = GetMaxAchievementsUser(
        gateway=gateway,
        service=AchievementUserService()
    )
    data = await handler()
    user_id, name, total = await gateway.get_max_achievements_user()
    assert data.id == user_id
    assert data.name == name
    assert data.count == total


async def test_get_max_achievements_user_invalid(
        achievement_users_gateway: AchievementUserGatewayMock
) -> None:
    gateway = achievement_users_gateway
    gateway.is_max_achievements_user = False
    handler = GetMaxAchievementsUser(
        gateway=gateway,
        service=AchievementUserService()
    )
    with pytest.raises(MaxAchievementsNotFound):
        await handler()
