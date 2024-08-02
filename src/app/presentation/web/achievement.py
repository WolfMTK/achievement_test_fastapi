from fastapi import APIRouter, Depends, HTTPException, status, Body, Query

from app.application.dto import (
    CreateAchievementDTO,
    AchievementResultDTO,
    Pagination,
    GetAchievementListDTO,
    AchievementListDTO,
    NewAchievementUserDTO,
    AchievementUserResultDTO,
)
from app.domain.exceptions import (
    AchievementExistsException,
    AchievementUserNotFoundException,
    AchievementUserExistsException
)
from app.presentation.interactors import (
    AchievementInteractorFactory,
    AchievementUserInteractorFactory,
)
from app.presentation.openapi import (
    EXAMPLE_CREATE_ACHIEVEMENT_BODY,
    EXAMPLE_CREATE_ACHIEVEMENT_RESPONSE,
    EXAMPLE_GET_ACHIEVEMENTS_RESPONSE,
    EXAMPLE_ADD_ACHIEVEMENT_USER_BODY,
    EXAMPLE_ADD_ACHIEVEMENT_USER_RESPONSE,
)

achievement_router = APIRouter(prefix='/achievement', tags=['Achievement'])


@achievement_router.post(
    '/',
    name='Добавить достижения',
    response_model=AchievementResultDTO,
    status_code=status.HTTP_201_CREATED,
    responses=EXAMPLE_CREATE_ACHIEVEMENT_RESPONSE
)
async def create_achievement(
        achievement: CreateAchievementDTO = Body(
            ...,
            example=EXAMPLE_CREATE_ACHIEVEMENT_BODY),
        ioc: AchievementInteractorFactory = Depends()
):
    """
    Добавление достижений.

    * **name** - название достижения (указывать RU|EN версии)

    * **numberPoints** - количество очков

    * **description** - описание достижения (указывать RU|EN версии)
    """
    try:
        async with ioc.create_achievement() as create_achievement_factory:
            return await create_achievement_factory(achievement)
    except AchievementExistsException as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(err)
        )


@achievement_router.get(
    '/',
    name='Получить информацию о всех доступных достижениях',
    response_model=AchievementListDTO,
    responses=EXAMPLE_GET_ACHIEVEMENTS_RESPONSE
)
async def get_achievements(
        limit: int = Query(10, description='Лимит записей'),
        offset: int = Query(0, description='Текущая страница'),
        ioc: AchievementInteractorFactory = Depends()
):
    """
    Информация о всех доступных достижениях.

    * **limit** - лимит записей

    * **offset** - текущая страница
    """
    async with ioc.get_achievements() as get_achievements_factory:
        return await get_achievements_factory(
            GetAchievementListDTO(Pagination(limit=limit, offset=offset))
        )


@achievement_router.post(
    '/users',
    name='Выдать достижение пользователю.',
    response_model=AchievementUserResultDTO,
    status_code=status.HTTP_201_CREATED,
    responses=EXAMPLE_ADD_ACHIEVEMENT_USER_RESPONSE
)
async def add_achievement_user(
        achievement_user: NewAchievementUserDTO = Body(
            ...,
            example=EXAMPLE_ADD_ACHIEVEMENT_USER_BODY
        ),
        ioc: AchievementUserInteractorFactory = Depends()
):
    """
    Выдает достижение пользователю с сохранением времени выдачи.

    * **userId** - уникальный идентификатор пользователя

    * **achievementId** - уникальный идентификатор достижения
    """
    try:
        async with ioc.add_achievement_user() as add_achievement_user_factory:
            return await add_achievement_user_factory(achievement_user)
    except AchievementUserExistsException as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(err)
        )
    except AchievementUserNotFoundException as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(err)
        )
