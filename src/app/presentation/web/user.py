from fastapi import APIRouter, Depends, HTTPException, status, Path, Query

from app.application.dto import (
    UserInfoDTO,
    GetAchievementUserDTO,
    Pagination,
    AchievementUserListDTO
)
from app.domain.exceptions import (
    UserNotFoundException,
    MaxAchievementsNotFoundException
)
from app.domain.models import UserId
from app.presentation.interactors import (
    UserInteractorFactory,
    AchievementUserInteractorFactory
)
from app.presentation.openapi import EXAMPLE_GET_USER_INFO_RESPONSE

user_router = APIRouter(prefix='/users')


@user_router.get(
    '/{user_id}/info',
    tags=['Users'],
    response_model=UserInfoDTO,
    responses=EXAMPLE_GET_USER_INFO_RESPONSE
)
async def get_user_info(
        user_id: UserId = Path(
            ...,
            description='Уникальный идентификатор пользователя'
        ),
        ioc: UserInteractorFactory = Depends()
):
    """
    Информация о пользователе

    * **user_id** - уникальный идентификатор пользователя (UUID)
    """
    try:
        async with ioc.get_user_info() as get_user_info_factory:
            return await get_user_info_factory(user_id)
    except UserNotFoundException as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        )


@user_router.get(
    '/{user_id}/achievement',
    tags=['Users'],
    response_model=AchievementUserListDTO
)
async def get_achievements_user(
        limit: int = Query(10, description='Лимит записей'),
        offset: int = Query(0, description='Текущая страница'),
        user_id: UserId = Path(
            ...,
            description='Уникальный идентификатор пользователя'
        ),
        ioc: AchievementUserInteractorFactory = Depends()
):
    try:
        async with ioc.get_achievement_user() as get_achievement_user_factory:
            return await get_achievement_user_factory(GetAchievementUserDTO(
                user_id=user_id,
                pagination=Pagination(limit=limit,
                                      offset=offset)
            ))
    except UserNotFoundException as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(err)
        )


@user_router.get(
    '/top/achievement',
    tags=['Statistics'],
)
async def get_max_achievements_user(
        ioc: AchievementUserInteractorFactory = Depends()
):
    try:
        async with (ioc.get_max_achievements_user() as
                    get_max_achievements_user_factory):
            return await get_max_achievements_user_factory()
    except MaxAchievementsNotFoundException as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(err)
        )
