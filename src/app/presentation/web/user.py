from fastapi import APIRouter, Depends, HTTPException, status, Path, Query

from app.application.dto import (
    UserInfoDTO,
    GetAdvanceUserDTO,
    Pagination,
    AdvanceUserListDTO
)
from app.domain.exceptions import UserNotFoundException
from app.domain.models import UserId
from app.presentation.interactors import (
    UserInteractorFactory,
    AdvanceUserInteractorFactory
)
from app.presentation.openapi import EXAMPLE_GET_USER_INFO_RESPONSE

user_router = APIRouter(prefix='/users', tags=['User'])


@user_router.get(
    '/{user_id}/info',
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
    '/{user_id}/advances',
    response_model=AdvanceUserListDTO
)
async def get_advance_user(
        limit: int = Query(10, description='Лимит записей'),
        offset: int = Query(0, description='Текущая страница'),
        user_id: UserId = Path(
            ...,
            description='Уникальный идентификатор пользователя'
        ),
        ioc: AdvanceUserInteractorFactory = Depends()
):
    async with ioc.get_advance_user() as get_advance_user_factory:
        return await get_advance_user_factory(GetAdvanceUserDTO(
            user_id=user_id,
            pagination=Pagination(limit=limit,
                                  offset=offset)
        ))
