from dataclasses import dataclass

from .advance_id import AdvanceId


@dataclass
class Advances:
    """  Модель достижений. """

    id: AdvanceId
    # уникальный идентификатор
    name: str
    # название достижения
    number_points: str
    # количество баллов за достижение
    description: str
    # описание достижения
