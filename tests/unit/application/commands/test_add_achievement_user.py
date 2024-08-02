import pytest

from app.application.commands import AddAchievementUser
from app.application.dto import NewAchievementUserDTO
from app.domain.exceptions import (
    AchievementUserNotFoundException,
    AchievementUserExistsException
)
from app.domain.services import AchievementUserService
from tests.mocks.achievement_users import AchievementUserGatewayMock
from tests.mocks.uow import UoWMock


async def test_add_achievement_user(
        achievement_users_gateway: AchievementUserGatewayMock,
        uow: UoWMock
) -> None:
    gateway = achievement_users_gateway
    handler = AddAchievementUser(
        gateway=gateway,
        uow=uow,
        service=AchievementUserService()
    )
    data = NewAchievementUserDTO(
        user_id=gateway.user_id,
        achievement_id=gateway.achievement_id
    )
    data = await handler(data)
    assert data.user_id == gateway.user_id
    assert data.achievement_id == gateway.achievement_id
    assert data.date_on == gateway.date_on.strftime('%Y-%m-%d %H:%M')

    assert uow.commited is True
    assert uow.flushing is False
    assert uow.rolled_back is False


async def test_add_achievement_user_invalid_id(
        achievement_users_gateway: AchievementUserGatewayMock,
        uow: UoWMock
) -> None:
    gateway = achievement_users_gateway
    handler = AddAchievementUser(
        gateway=gateway,
        uow=uow,
        service=AchievementUserService()
    )
    data = NewAchievementUserDTO(
        user_id=gateway.user_id,
        achievement_id=gateway.achievement_id
    )
    gateway.is_user_id_and_achievement_id = False
    with pytest.raises(AchievementUserNotFoundException):
        await handler(data)

    assert uow.commited is False
    assert uow.flushing is False
    assert uow.rolled_back is False


async def test_add_achievement_user_invalid(
        achievement_users_gateway: AchievementUserGatewayMock,
        uow: UoWMock
) -> None:
    gateway = achievement_users_gateway
    handler = AddAchievementUser(
        gateway=gateway,
        uow=uow,
        service=AchievementUserService()
    )
    data = NewAchievementUserDTO(
        user_id=gateway.user_id,
        achievement_id=gateway.achievement_id
    )
    gateway.is_achievement_user = True
    with pytest.raises(AchievementUserExistsException):
        await handler(data)

    assert uow.commited is False
    assert uow.flushing is False
    assert uow.rolled_back is False
