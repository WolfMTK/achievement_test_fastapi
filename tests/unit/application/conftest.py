import pytest

from tests.mocks.achievement import AchievementGatewayMock
from tests.mocks.achievement_users import AchievementUserGatewayMock
from tests.mocks.uow import UoWMock
from tests.mocks.user import UserGatewayMock


@pytest.fixture()
def achievement_gateway() -> AchievementGatewayMock:
    return AchievementGatewayMock()


@pytest.fixture()
def achievement_users_gateway() -> AchievementUserGatewayMock:
    return AchievementUserGatewayMock()


@pytest.fixture()
def user_gateway() -> UserGatewayMock:
    return UserGatewayMock()


@pytest.fixture()
def uow() -> UoWMock:
    return UoWMock()
