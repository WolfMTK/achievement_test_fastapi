from dataclasses import dataclass

from app.domain.enums import Language
from app.domain.models.user_id import UserId


@dataclass
class Users:
    """ Модель пользователей. """

    id: UserId
    # уникальный идентификатор
    name: str
    # имя пользователя
    language: Language
    # выбранный пользователем язык
