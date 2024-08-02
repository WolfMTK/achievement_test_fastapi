from app.application.commands import GetUsersWithDaysStreak
from tests.mocks.achievement_users import AchievementUserGatewayMock


async def test_get_users_with_days_streak(
        achievement_users_gateway: AchievementUserGatewayMock
) -> None:
    gateway = achievement_users_gateway
    handler = GetUsersWithDaysStreak(
        gateway=gateway
    )
    data = await handler()
    total = len(await gateway.get_users_with_days_streak())
    assert len(data) == total
