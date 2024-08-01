from fastapi import APIRouter, Depends, HTTPException, status, Path, Query

from app.application.dto import (
    UserInfoDTO,
    GetAchievementUserDTO,
    Pagination,
    AchievementUserListDTO,
    MaxAchievementsUserResultDTO,
    MaxAchievementPointsUserResultDTO,
    UserWithMaxPointsDiffResultDTO,
    UserWithMinPointsDiffResultDTO
)
from app.domain.exceptions import (
    UserNotFoundException,
    MaxAchievementsNotFound,
    MaxPointsNotFound,
    MaxPointsDiffNotFoundException,
    MinPointsDiffNotFoundException
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
    '/top',
    tags=['Statistics'],
    response_model=MaxAchievementsUserResultDTO
)
async def get_max_achievements_user(
        ioc: AchievementUserInteractorFactory = Depends()
):
    try:
        async with (ioc.get_max_achievements_user() as
                    get_max_achievements_user_factory):
            return await get_max_achievements_user_factory()
    except MaxAchievementsNotFound as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(err)
        )


@user_router.get(
    '/top-points',
    tags=['Statistics'],
    response_model=MaxAchievementPointsUserResultDTO
)
async def get_max_achievement_points_user(
        ioc: AchievementUserInteractorFactory = Depends()
):
    try:
        async with (ioc.get_max_achievement_points_user() as
                    get_max_achievements_user_factory):
            return await get_max_achievements_user_factory()
    except MaxPointsNotFound as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(err)
        )


@user_router.get(
    '/max-diff-points',
    tags=['Statistics'],
    response_model=list[UserWithMaxPointsDiffResultDTO]
)
async def get_users_with_max_points_diff(
        ioc: AchievementUserInteractorFactory = Depends()
):
    try:
        async with (ioc.get_users_with_max_points_diff() as
                    get_users_with_max_points_diff_factory):
            return await get_users_with_max_points_diff_factory()
    except MaxPointsDiffNotFoundException as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(err)
        )


@user_router.get(
    '/min-diff-points',
    tags=['Statistics'],
    response_model=list[UserWithMinPointsDiffResultDTO]
)
async def get_users_with_min_points_diff(
        ioc: AchievementUserInteractorFactory = Depends()
):
    try:
        async with (ioc.get_users_with_min_points_diff() as
                    get_users_with_min_points_diff_factory):
            return await get_users_with_min_points_diff_factory()
    except MinPointsDiffNotFoundException as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(err)
        )


@user_router.get(
    '/days-streak',
    tags=['Statistics'],
    response_model=list[UserInfoDTO]
)
async def get_users_with_days_streak(
        ioc: AchievementUserInteractorFactory = Depends()
):
    async with (ioc.get_users_with_days_streak() as
                get_users_with_days_streak_factory):
        return await get_users_with_days_streak_factory()
