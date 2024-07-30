import uuid
from collections.abc import Iterator
from typing import cast

from app.domain.exceptions import AdvanceExistsException
from app.domain.models import Advances, AdvanceId


class AdvanceService:
    def get_advances(self, advances: Iterator[Advances]) -> list[Advances]:
        return [Advances(id=val.id,
                         name=val.name,
                         number_points=val.number_points,
                         description=val.description) for val in advances]

    def check_advance(self, value: bool) -> None:
        if value:
            raise AdvanceExistsException()

    def create_advance(self, name: str, number_points: int, description: str):
        advance_id = cast(AdvanceId, uuid.uuid4())
        return Advances(id=advance_id,
                        name=name,
                        number_points=number_points,
                        description=description)
