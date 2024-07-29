from dataclasses import dataclass

from app.domain.enums import Language
from app.domain.models.user_id import UserId


@dataclass
class Users:
    id: UserId
    name: str
    language: Language
