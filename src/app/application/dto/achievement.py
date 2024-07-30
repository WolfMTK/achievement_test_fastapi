from dataclasses import dataclass

from pydantic import Field, field_validator

from app.core.constants import LENGTH_LANGUAGE, RU_LOWERCASE, EN_LOWERCASE
from app.core.validators import check_text
from app.domain.models import AchievementId, Achievements
from .base import Base
from .pagination import Pagination


@dataclass
class GetAchievementListDTO:
    """ Модель данных для получения списка достижений. """

    pagination: Pagination


class CreateAchievementDTO(Base):
    """ Модель данных для создания достижений. """

    name: str = Field(..., description='Название достижения')
    number_points: int = Field(
        ..., description='Количество баллов за достижение'
    )
    description: str = Field(
        ..., description='Описание достижения'
    )

    @field_validator('name', 'description')
    @classmethod
    def validate_name(cls, text: str) -> str:
        return cls._validate_text(text)

    @classmethod
    def _validate_text(cls, text: str) -> str:
        name_split = text.replace(' |', '|').replace('| ', '|').split('|')
        if len(name_split) != LENGTH_LANGUAGE:
            raise ValueError('Достижения должны быть на двух языках')
        result = {'ru': '', 'en': ''}
        for index, val in enumerate(name_split):
            if val == '':
                raise ValueError('Достижения должны быть на двух языках')
            if check_text(val, RU_LOWERCASE):
                result['ru'] = val
            elif check_text(val, EN_LOWERCASE):
                result['en'] = val
        return '|'.join(result.values())


class AchievementResultDTO(Base):
    """ Модель данных для получения достижений. """

    id: AchievementId = Field(...,
                              description='Уникальный идентификатор')


class AchievementListDTO(Base):
    """ Модель данных для получения массива достижений. """

    total: int = Field(..., description='Количество достижений')
    limit: int = Field(..., description='Лимит записей')
    offset: int = Field(..., description='Текущая страница')
    achievements: list[Achievements]
