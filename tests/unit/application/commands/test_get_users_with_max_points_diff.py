import pytest

from app.application.commands import GetUsersWithMaxPointsDiff
from app.domain.exceptions import MaxPointsDiffNotFoundException
from app.domain.services import AchievementUserService
from tests.mocks.achievement_users import AchievementUserGatewayMock


async def test_get_users_with_max_points_diff(
        achievement_users_gateway: AchievementUserGatewayMock
) -> None:
    gateway = achievement_users_gateway
    handler = GetUsersWithMaxPointsDiff(
        gateway=gateway,
        service=AchievementUserService()
    )
    data = await handler()
    users = await gateway.get_users_with_max_points_diff()
    assert len(data) == len(users)

    user_id, name, total, max_diff = users[0]
    data = data[0]
    # минус данной проверки, что данные могут не совпасть
    assert data.id == user_id
    assert data.name == name
    assert data.total_points == total
    assert data.max_diff == max_diff


async def test_get_users_with_max_points_diff_invalid(
        achievement_users_gateway: AchievementUserGatewayMock
) -> None:
    gateway = achievement_users_gateway
    gateway.is_user_with_max_points_diff = False
    handler = GetUsersWithMaxPointsDiff(
        gateway=gateway,
        service=AchievementUserService()
    )
    with pytest.raises(MaxPointsDiffNotFoundException):
        await handler()
