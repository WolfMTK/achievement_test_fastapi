from sqlalchemy.orm import Mapped, mapped_column

from app.domain.enums import Language
from .base import BaseModel


class Users(BaseModel):
    """ Модель пользователей. """

    name: Mapped[str] = mapped_column(nullable=False,
                                      comment='Имя пользователя')
    language: Mapped[Language] = mapped_column(nullable=False,
                                               default=Language.RU,
                                               comment='Выбранный пользователем язык')
