from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class Advances(BaseModel):
    """ Модель достижений. """

    name: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
        comment='Название достижения'
    )
    number_points: Mapped[str] = mapped_column(
        nullable=False,
        comment='Количество баллов за достижения'
    )
    description: Mapped[str] = mapped_column(
        nullable=False,
        comment='Описание достижения'
    )
