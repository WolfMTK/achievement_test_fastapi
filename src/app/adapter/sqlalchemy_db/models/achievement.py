import uuid

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .achievement_user import UsersAchievements
from .base import BaseModel


class Achievements(BaseModel):
    """ Модель достижений. """

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
        comment='Уникальный идентификатор',
        autoincrement=False  # Генерация ID будет происходить не на стороне БД
    )
    name: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
        comment='Название достижения'
    )
    number_points: Mapped[int] = mapped_column(
        nullable=False,
        comment='Количество баллов за достижения'
    )
    description: Mapped[str] = mapped_column(
        Text(),
        nullable=False,
        comment='Описание достижения'
    )
    users: Mapped[list[UsersAchievements]] = relationship(
        back_populates='achievement'
    )
