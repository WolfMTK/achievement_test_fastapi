from pydantic import Field

from app.domain.enums import Language
from app.domain.models import UserId
from .base import Base


class UserInfoDTO(Base):
    id: UserId = Field(..., description='Уникальный идентификатор')
    name: str = Field(..., description='Имя пользователя')
    language: Language = Field(...,
                               description='Выбранный пользователем язык')
