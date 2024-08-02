import uuid
from typing import Any

from app.adapter.stubs import StubAchievementGateway
from app.domain.models import Achievements


class AchievementGatewayMock(StubAchievementGateway):
    def __init__(self) -> None:
        self._user_uuid = uuid.uuid4()
        self._achievement_uuid = uuid.uuid4()
        self._total = 4
        self.is_check = False

    @property
    def total(self) -> int:
        return self._total

    @property
    def user_uuid(self) -> uuid.uuid4():
        return self._user_uuid

    async def create(self, *args: Any, **kwargs: Any) -> Achievements:
        return Achievements(
            id=self.user_uuid,
            name='test|тест',
            number_points=10,
            description='test|тест'
        )

    async def get_all(
            self,
            limit: int,
            offset: int
    ) -> list[Achievements]:
        achievements = [
            Achievements(
                id=uuid.uuid4(),
                name='test|тест',
                number_points=10,
                description='test|тест'
            ),
            Achievements(
                id=uuid.uuid4(),
                name='test1|тест1',
                number_points=10,
                description='test1|тест1'
            ),
            Achievements(
                id=uuid.uuid4(),
                name='test2|тест2',
                number_points=10,
                description='test2|тест2'
            ),
            Achievements(
                id=uuid.uuid4(),
                name='test3|тест3',
                number_points=10,
                description='test3|тест3'
            )
        ]
        return achievements[offset:limit + offset]

    async def get_total_achievements(self) -> int:
        return self.total

    async def check_achievement(self, *args: Any, **kwargs: Any) -> bool:
        return self.is_check
