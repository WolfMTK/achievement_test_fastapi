from dataclasses import dataclass

from pydantic import Field

from app.domain.models import UserId, AchievementId, Achievements
from .pagination import Pagination
from .base import BaseModel


class NewAchievementUserDTO(BaseModel):
    """ Модель данных для добавления достижения пользователю. """

    user_id: UserId = Field(
        ...,
        description='Уникальный идентификатор пользователя',
    )
    achievement_id: AchievementId = Field(
        ...,
        description='Уникальный идентификатор достижения',
    )


class AchievementUserResultDTO(NewAchievementUserDTO):
    """ Модель данных для получения достижения пользователя. """

    date_on: str = Field(
        ...,
        description='Дата выдачи достижения'
    )


class AchievementUserListDTO(BaseModel):
    total: int = Field(..., description='Количество достижений')
    limit: int = Field(..., description='Лимит записей')
    offset: int = Field(..., description='Текущая страница')
    user_id: UserId = Field(
        ...,
        description='Уникальный идентификатор пользователя',
    )
    achievements: list[Achievements]



@dataclass
class GetAchievementUserDTO:
    """ Модель данных для получения достижений пользователя. """

    user_id: UserId
    pagination: Pagination
