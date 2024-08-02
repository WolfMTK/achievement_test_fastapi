import pytest

from app.application.commands import GetMaxAchievementPointsUser
from app.domain.exceptions import MaxPointsNotFound
from app.domain.services import AchievementUserService
from tests.mocks.achievement_users import AchievementUserGatewayMock


async def test_get_max_achievement_points_user(
        achievement_users_gateway: AchievementUserGatewayMock
) -> None:
    gateway = achievement_users_gateway
    handler = GetMaxAchievementPointsUser(
        gateway=gateway,
        service=AchievementUserService()
    )
    data = await handler()
    user_id, name, total = await gateway.get_max_achievement_points_user()
    assert data.id == user_id
    assert data.name == name
    assert data.total_points == total


async def test_get_max_achievements_points_user_invalid(
        achievement_users_gateway: AchievementUserGatewayMock
) -> None:
    gateway = achievement_users_gateway
    gateway.is_max_achievement_points = False
    handler = GetMaxAchievementPointsUser(
        gateway=gateway,
        service=AchievementUserService()
    )
    with pytest.raises(MaxPointsNotFound):
        await handler()
