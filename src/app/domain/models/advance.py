from dataclasses import dataclass

from .advance_id import AdvanceId


@dataclass
class Advances:
    """  Модель достижений. """

    id: AdvanceId
    # уникальный идентификатор
    name: str
    # название достижения
    number_points: int
    # количество баллов за достижение
    description: str
    # описание достижения

    def __post_init__(self):
        self.number_points = int(self.number_points)
