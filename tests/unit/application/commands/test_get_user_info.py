import pytest

from app.application.commands import GetUserInfo
from app.domain.exceptions import UserNotFoundException
from app.domain.services import UserService
from tests.mocks.user import UserGatewayMock


async def test_get_user_info(
        user_gateway: UserGatewayMock
) -> None:
    gateway = user_gateway
    handler = GetUserInfo(
        gateway=gateway,
        service=UserService()
    )
    user = await gateway.get()
    data = await handler(user.id)
    assert data.id == user.id
    assert data.name == user.name
    assert data.language == user.language


async def test_get_user_info_invalid(
        user_gateway: UserGatewayMock
) -> None:
    gateway = user_gateway
    handler = GetUserInfo(
        gateway=gateway,
        service=UserService()
    )
    gateway.is_user = False
    with pytest.raises(UserNotFoundException):
        await handler(gateway.user_id)
