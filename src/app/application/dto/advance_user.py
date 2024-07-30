from dataclasses import dataclass

from pydantic import Field

from app.domain.models import UserId, AdvanceId, Advances
from .pagination import Pagination
from .base import BaseModel


class NewAdvanceUserDTO(BaseModel):
    """ Модель данных для добавления достижения пользователю. """

    user_id: UserId = Field(
        ...,
        description='Уникальный идентификатор пользователя',
    )
    advance_id: AdvanceId = Field(
        ...,
        description='Уникальный идентификатор достижения',
    )


class AdvanceUserResultDTO(NewAdvanceUserDTO):
    """ Модель данных для получения достижения пользователя. """

    date_on: str = Field(
        ...,
        description='Дата выдачи достижения'
    )


class AdvanceUserListDTO(BaseModel):
    total: int = Field(..., description='Количество достижений')
    limit: int = Field(..., description='Лимит записей')
    offset: int = Field(..., description='Текущая страница')
    user_id: UserId = Field(
        ...,
        description='Уникальный идентификатор пользователя',
    )
    advances: list[Advances]



@dataclass
class GetAdvanceUserDTO:
    """ Модель данных для получения достижений пользователя. """

    user_id: UserId
    pagination: Pagination
