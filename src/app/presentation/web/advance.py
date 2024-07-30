from fastapi import APIRouter, Depends, HTTPException, status, Body, Query

from app.application.dto import (
    CreateAdvanceDTO,
    AdvanceResultDTO,
    Pagination,
    GetAdvanceListDTO,
    AdvanceListDTO,
    NewAdvanceUserDTO,
    AdvanceUserResultDTO,
)
from app.domain.exceptions import (
    AdvanceExistsException,
    AdvanceUserNotFoundException,
    AdvanceUserExistsException
)
from app.presentation.interactors import (
    AdvanceInteractorFactory,
    AdvanceUserInteractorFactory,
)
from app.presentation.openapi import (
    EXAMPLE_CREATE_ADVANCE_BODY,
    EXAMPLE_CREATE_ADVANCE_RESPONSE,
    EXAMPLE_GET_ADVANCES_RESPONSE,
)

advance_router = APIRouter(prefix='/advance', tags=['Advance'])


@advance_router.post(
    '/',
    response_model=AdvanceResultDTO,
    status_code=status.HTTP_201_CREATED,
    responses=EXAMPLE_CREATE_ADVANCE_RESPONSE
)
async def create_advance(
        advance: CreateAdvanceDTO = Body(
            ...,
            example=EXAMPLE_CREATE_ADVANCE_BODY),
        ioc: AdvanceInteractorFactory = Depends()
):
    try:
        async with ioc.create_advance() as create_advance_factory:
            return await create_advance_factory(advance)
    except AdvanceExistsException as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(err)
        )


@advance_router.get(
    '/',
    response_model=AdvanceListDTO,
    responses=EXAMPLE_GET_ADVANCES_RESPONSE
)
async def get_advances(
        limit: int = Query(10, description='Лимит записей'),
        offset: int = Query(0, description='Текущая страница'),
        ioc: AdvanceInteractorFactory = Depends()
):
    async with ioc.get_advances() as get_advances_factory:
        return await get_advances_factory(
            GetAdvanceListDTO(Pagination(limit=limit, offset=offset))
        )


@advance_router.post(
    '/users',
    response_model=AdvanceUserResultDTO,
    status_code=status.HTTP_201_CREATED
)
async def add_advance_user(
        advance_user: NewAdvanceUserDTO,
        ioc: AdvanceUserInteractorFactory = Depends()
):
    try:
        async with ioc.add_advance_user() as add_advance_user_factory:
            return await add_advance_user_factory(advance_user)
    except AdvanceUserExistsException as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(err)
        )
    except AdvanceUserNotFoundException as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(err)
        )
