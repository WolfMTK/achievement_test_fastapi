from dataclasses import dataclass

from .achievement_id import AchievementId


@dataclass
class Achievements:
    """  Модель достижений. """

    id: AchievementId
    # уникальный идентификатор
    name: str
    # название достижения
    number_points: int
    # количество баллов за достижение
    description: str
    # описание достижения
