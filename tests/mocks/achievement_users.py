import datetime as dt
import uuid
from typing import Any

from app.adapter.stubs import StubAchievementUserGateway
from app.domain.enums import Language
from app.domain.models import (
    UsersAchievements,
    UserId,
    AchievementId,
    Achievements,
    Users
)


class AchievementUserGatewayMock(StubAchievementUserGateway):
    def __init__(self):
        self._date_on = dt.datetime.now()
        self._user_id = uuid.uuid4()
        self._achievement_id = uuid.uuid4()
        self._total = 2
        self.is_user_exists = True
        self.is_achievement_user = False
        self.is_max_achievement_points = True
        self.is_user_id_and_achievement_id = True
        self.is_max_achievements_user = True
        self.is_user_with_max_points_diff = True
        self.is_user_with_min_points_diff = True

    @property
    def date_on(self) -> dt.datetime:
        return self._date_on

    @property
    def user_id(self) -> uuid.UUID:
        return self._user_id

    @property
    def achievement_id(self) -> uuid.UUID:
        return self._achievement_id

    @property
    def total(self) -> int:
        return self._total

    async def create(self, *args: Any, **kwargs: Any) -> UsersAchievements:
        return UsersAchievements(
            user_id=self.user_id,
            achievement_id=self.achievement_id,
            date_on=self.date_on,
            achievement=None,
            user=None
        )

    async def get_achievements(
            self,
            user_id: UserId,
            limit: int,
            offset: int
    ) -> list[UsersAchievements]:
        users_achievements = [
            UsersAchievements(
                user_id=self.user_id,
                achievement_id=self.achievement_id,
                date_on=self.date_on,
                achievement=Achievements(
                    id=self.achievement_id,
                    name='тест|test',
                    number_points=10,
                    description='тест|test'
                ),
                user=Users(
                    id=self.user_id,
                    name='test',
                    language='RU'
                )
            ),
            UsersAchievements(
                user_id=self.user_id,
                achievement_id=self.achievement_id,
                date_on=self.date_on,
                achievement=Achievements(
                    id=self.achievement_id,
                    name='тест|test',
                    number_points=10,
                    description='тест|test'
                ),
                user=Users(
                    id=self.user_id,
                    name='test',
                    language='RU'
                )
            )
        ]
        return users_achievements

    async def check_user_id_and_achievement_id(
            self,
            user_id: UserId,
            achievement_id: AchievementId
    ) -> bool:
        return self.is_user_id_and_achievement_id

    async def check_achievement_user(
            self,
            user_id: UserId,
            achievement_id: AchievementId
    ) -> bool:
        return self.is_achievement_user

    async def get_total_achievements(self, user_id: UserId) -> int:
        return self._total

    async def get_max_achievement_points_user(
            self
    ) -> tuple[UserId, str, int] | None:
        if self.is_max_achievement_points:
            return (self.user_id, 'test', 10)
        return None

    async def check_user_exists(self, user_id: UserId) -> bool:
        return self.is_user_exists

    async def get_max_achievements_user(
            self
    ) -> tuple[UserId, str, int] | None:
        if self.is_max_achievements_user:
            return (self.user_id, 'test', 10)
        return None

    async def get_users_with_days_streak(self) -> list[Users]:
        users = [
            Users(
                id=self.user_id,
                name='test',
                language=Language.RU
            ),
            Users(
                id=uuid.uuid4(),
                name='test',
                language=Language.RU
            )
        ]
        return users

    async def get_users_with_min_points_diff(
            self
    ) -> list[tuple[UserId, str, int, int]] | None:
        if self.is_user_with_min_points_diff:
            return [
                (self.user_id, 'test', 1250, 90),
                (uuid.uuid4(), 'test', 1160, 90)
            ]
        return None

    async def get_users_with_max_points_diff(
            self
    ) -> list[tuple[UserId, str, int, int]] | None:
        if self.is_user_with_max_points_diff:
            return [
                (self.user_id, 'test', 1250, 90),
                (uuid.uuid4(), 'test', 1160, 90)
            ]
        return None
