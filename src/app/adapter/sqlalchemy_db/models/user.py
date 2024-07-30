import uuid

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.enums import Language
from .achievement_user import UsersAchievements
from .base import BaseModel


class Users(BaseModel):
    """ Модель пользователей. """

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
        comment='Уникальный идентификатор',
        autoincrement=False  # Генерация ID будет происходить не на стороне БД
    )
    name: Mapped[str] = mapped_column(nullable=False,
                                      comment='Имя пользователя')
    language: Mapped[Language] = mapped_column(nullable=False,
                                               default=Language.RU,
                                               comment='Выбранный пользователем язык')
    achievements: Mapped[list[UsersAchievements]] = relationship(back_populates='user',
                                                                 lazy='selectin')
