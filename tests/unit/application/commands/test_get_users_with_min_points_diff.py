import pytest

from app.application.commands import GetUsersWithMinPointsDiff
from app.domain.exceptions import MinPointsDiffNotFoundException
from app.domain.services import AchievementUserService
from tests.mocks.achievement_users import AchievementUserGatewayMock


async def test_get_users_with_min_diff(
        achievement_users_gateway: AchievementUserGatewayMock
) -> None:
    gateway = achievement_users_gateway
    handler = GetUsersWithMinPointsDiff(
        gateway=gateway,
        service=AchievementUserService()
    )
    data = await handler()
    users = await gateway.get_users_with_min_points_diff()
    assert len(data) == len(users)

    user_id, name, total, min_diff = users[0]
    data = data[0]
    # минус данной проверки, что данные могут не совпасть
    assert data.id == user_id
    assert data.name == name
    assert data.total_points == total
    assert data.min_diff == min_diff


async def test_get_users_with_min_diff_invalid(
        achievement_users_gateway: AchievementUserGatewayMock
) -> None:
    gateway = achievement_users_gateway
    gateway.is_user_with_min_points_diff = False
    handler = GetUsersWithMinPointsDiff(
        gateway=gateway,
        service=AchievementUserService()
    )
    with pytest.raises(MinPointsDiffNotFoundException):
        await handler()
