from dataclasses import dataclass

from pydantic import Field

from app.domain.models import UserId, AchievementId, Achievements
from .base import Base
from .pagination import Pagination


class NewAchievementUserDTO(Base):
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


class AchievementUserListDTO(Base):
    """ Модель данных для получения массива достижения пользователя. """

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


class MaxAchievementsUserResultDTO(Base):
    """
    Модель данных для получения пользователя
    с максимальным количеством достижений.
    """

    id: UserId = Field(
        ...,
        description='Уникальный идентификатор пользователя',
    )
    name: str = Field(
        ...,
        description='Имя пользователя'
    )
    count: int = Field(
        ...,
        description='Количество достижений'
    )


class MaxAchievementPointsUserResultDTO(Base):
    """
    Модель данных для получения пользователя с максимальным
    количеством очков достижений.
    """
    id: UserId = Field(
        ...,
        description='Уникальный идентификатор пользователя',
    )
    name: str = Field(
        ...,
        description='Имя пользователя'
    )
    total_points: int = Field(
        ...,
        description='Количеством очков достижений'
    )


class UserWithMaxPointsDiffResultDTO(MaxAchievementPointsUserResultDTO):
    """
    Модель данных для получения пользователя
    с максимальной разностью очков.
    """
    max_diff: int = Field(
        ...,
        description='Максимальная разность очков'
    )


class UserWithMinPointsDiffResultDTO(MaxAchievementPointsUserResultDTO):
    """
    Модель данных для получения пользователя
    с минимальной разностью очков.
    """
    min_diff: int = Field(
        ...,
        description='Минимальная разность очков'
    )
