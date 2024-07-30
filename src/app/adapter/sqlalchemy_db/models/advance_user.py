import datetime as dt
import uuid
from typing import TypeVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel

Users = TypeVar('Users')
Advances = TypeVar('Advances')


class UsersAchievements(BaseModel):
    """ Ассоциативная таблица между пользователями и достижениями. """

    __tablename__ = 'users_advances'
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('users.id'),
        primary_key=True
    )
    advance_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('advances.id'),
        primary_key=True
    )
    date_on: Mapped[dt.datetime] = mapped_column(
        nullable=False,
        default=dt.datetime.now,
        comment='Дата выдачи достижения'
    )
    user: Mapped['Users'] = relationship(back_populates='advances',
                                         lazy='selectin')
    advance: Mapped['Advances'] = relationship(back_populates='users',
                                               lazy='selectin')
