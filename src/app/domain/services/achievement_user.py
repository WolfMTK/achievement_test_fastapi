import datetime as dt
from collections.abc import Iterator

from app.core.constants import LANGUAGE
from app.domain.exceptions import (
    AchievementUserExistsException,
    AchievementUserNotFoundException,
)
from app.domain.models import UsersAchievements, Achievements


class AchievementUserService:
    def check_achievement_and_user(self, value) -> None:
        if not value:
            raise AchievementUserNotFoundException()

    def check_achievement_user(self, value: bool) -> None:
        if value:
            raise AchievementUserExistsException()

    def get_date_on(self, date_on: dt.datetime) -> str:
        return date_on.strftime('%Y-%m-%d %H:%M')

    def get_achievement(
            self,
            data: Iterator[UsersAchievements]
    ) -> list[Achievements]:
        result = []
        for val in data:
            achievement = val.achievement
            language = val.user.language
            name = achievement.name.split('|')[LANGUAGE[language.lower()]]
            description = achievement.description.split('|')[LANGUAGE[language.lower()]]
            result.append(
                Achievements(
                    id=achievement.id,
                    name=name,
                    number_points=achievement.number_points,
                    description=description
                )
            )
        return result
