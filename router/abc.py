from typing import List
from fastapi import APIRouter, Depends, status
from db import db_abc
from sqlalchemy.ext.asyncio.session import AsyncSession
from db.database import get_async_db
from schemas.schemas_abc import AbcModel, AbcDisplay

router = APIRouter(prefix="/user", tags=["user"])


@router.post(
    "/create",
    deprecated=False,
    name='Abc_Creation',
    summary="une phrase qui resume la fonction.",
    description="une decription longue et precise?",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
    response_description="Succes de la reponse",
    responses={
        201: {
            "description": "SUCCESS - Abc has been created",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "New Abc has been succefully added to the database."
                    }
                }
            }
        }
    }
)
async def create(request: AbcModel, db: AsyncSession = Depends(get_async_db)):
    abc = await db_abc.create(request, db)
    return abc

#--------------------------------------------------------------------------

@router.get(
    "/read_abc_by_abc",
    deprecated=False,
    name='Abc_read_by_abc',
    summary="une phrase qui resume la fonction.",
    description="une decription longue et precise?",
    response_model=List[AbcDisplay],
    status_code=status.HTTP_200_OK,
    response_description="Succes de la reponse",
    responses={
        200: {
            "description": "SUCCESS - Abc has been Found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Abc has been succefully found in the database."
                    }
                }
            }
        }
    }
)
async def read_abc_by_abc(abc: str, db: AsyncSession = Depends(get_async_db)):
    abc = await db_abc.read_abc_by_abc(abc, db)
    return abc


#--------------------------------------------------------------------------


@router.get(
    "/read_all_abc",
    deprecated=False,
    name='abc_read_all',
    summary="une phrase qui resume la fonction.",
    description="une decription longue et precise?",
    response_model=List[AbcDisplay],
    status_code=status.HTTP_200_OK,
    response_description="Succes de la reponse",
    responses={
        200: {
            "description": "SUCCESS - abc has been Found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "abc has been succefully found in the database."
                    }
                }
            }
        }
    }
)
async def read_all_abc(db: AsyncSession = Depends(get_async_db)):
    abc = await db_abc.read_all_abc(db)
    return abc


#--------------------------------------------------------------------------

@router.put(
    "/update",
    deprecated=False,
    name='abc_update',
    summary="une phrase qui resume la fonction.",
    description="une decription longue et precise?",
    response_model=None,
    status_code=status.HTTP_200_OK,
    response_description="Succes de la reponse",
    responses={
        200: {
            "description": "SUCCESS - abc has been Updated",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "abc has been succefully updated to the database."
                    }
                }
            }
        }
    }
)
async def update(id: int, request: AbcModel, db: AsyncSession = Depends(get_async_db)):
    abc = await db_abc.update(id, request, db)
    return abc

#--------------------------------------------------------------------------

@router.delete(
    "/delete",
    deprecated=False,
    name='abc_delete',
    summary="une phrase qui resume la fonction.",
    description="une decription longue et precise?",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="Succes de la reponse",
    responses={
        204: {
            "description": "SUCCES - abc has been delete",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "abc has been succefully delete from the database."
                    }
                }
            }
        },
        500: {
            "description": "SQLAlchemyError - abc FAILED to be deleted!",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Error - abc has FAILED to be delete from the database."
                    }
                }
            }
        }
    }
)
async def delete(id: int, db: AsyncSession = Depends(get_async_db)):
    await db_abc.delete(id, db)
    return None