import datetime as dt
from collections.abc import Iterator

from app.core.constants import LANGUAGE
from app.domain.exceptions import (
    AdvanceUserExistsException,
    AdvanceUserNotFoundException,
)
from app.domain.models import UsersAdvances, Advances


class AdvanceUserService:
    def check_advance_and_user(self, value) -> None:
        if not value:
            raise AdvanceUserNotFoundException()

    def check_advance_user(self, value: bool) -> None:
        if value:
            raise AdvanceUserExistsException()

    def get_date_on(self, date_on: dt.datetime) -> str:
        return date_on.strftime('%Y-%m-%d %H:%M')

    def get_advances(self, data: Iterator[UsersAdvances]) -> list[Advances]:
        result = []
        for val in data:
            advance = val.advance
            language = val.user.language
            name = advance.name.split('|')[LANGUAGE[language.lower()]]
            description = advance.description.split('|')[LANGUAGE[language.lower()]]
            result.append(
                Advances(
                    id=advance.id,
                    name=name,
                    number_points=advance.number_points,
                    description=description
                )
            )
        return result
