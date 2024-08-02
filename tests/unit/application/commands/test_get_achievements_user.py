import pytest

from app.application.commands import GetAchievementsUser
from app.application.dto import GetAchievementUserDTO, Pagination
from app.domain.exceptions import UserNotFoundException
from app.domain.services import AchievementUserService
from tests.mocks.achievement_users import AchievementUserGatewayMock


async def test_get_achievements_user(
        achievement_users_gateway: AchievementUserGatewayMock
) -> None:
    gateway = achievement_users_gateway
    handler = GetAchievementsUser(
        gateway=gateway,
        service=AchievementUserService()
    )
    limit = 10
    offset = 0
    data = GetAchievementUserDTO(
        user_id=gateway.user_id,
        pagination=Pagination(
            limit=limit,
            offset=offset
        )
    )
    data = await handler(data)
    assert data.total == gateway.total
    assert data.limit == limit
    assert data.offset == offset
    assert data.user_id == gateway.user_id
    assert len(data.achievements) == gateway.total


async def test_get_achievements_user_invalid(
        achievement_users_gateway: AchievementUserGatewayMock
) -> None:
    gateway = achievement_users_gateway
    gateway.is_user_exists = False
    handler = GetAchievementsUser(
        gateway=gateway,
        service=AchievementUserService()
    )
    data = GetAchievementUserDTO(
        user_id=gateway.user_id,
        pagination=Pagination(
            limit=10,
            offset=0
        )
    )
    with pytest.raises(UserNotFoundException):
        await handler(data)
