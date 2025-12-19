from fastapi import Depends, HTTPException, status
from db.database import get_async_db
from db.models import DbAbc
from schemas.schemas_abc import AbcModel
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy import exc, select, update as sql_update, delete as sql_delete


async def create(
        request: AbcModel,
        db: AsyncSession = Depends(get_async_db)):
    try:
        new_user = DbAbc(
            abc=request.username,
        )
        db.add(new_user)
        await db.commit()
    except exc.SQLAlchemyError as e:
        await db.rollback()
        print(f"Database error during creation: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while saving changes to the database.",
        )
    return {"detail": "New User has been successfully added to the database."}


# --------------------------------------------------------------------------


async def read_user_by_username(
    abc: str,
    db: AsyncSession = Depends(get_async_db)
):
    query = select(AbcModel).where(AbcModel.abc == abc)
    result = await db.execute(query)
    user = result.scalars().all()
    return user

# --------------------------------------------------------------------------


async def read_all_users(
    db: AsyncSession = Depends(get_async_db)
):
    query = select(AbcModel)
    result = await db.execute(query)
    user = result.scalars().all()
    return user


# --------------------------------------------------------------------------


async def update(
        id: int,
        request: AbcModel,
        db: AsyncSession = Depends(get_async_db)):
    try:
        query = (
            sql_update(AbcModel)
            .where(AbcModel.id == id)
            .values(
                abc=request.username,
            )
        )

        await db.execute(query)
        await db.commit()
    except exc.SQLAlchemyError as e:
        await db.rollback()
        print(f"Database error during creation: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while saving changes to the database.",
        )
    return {"detail": "New User has been successfully added to the database."}


# --------------------------------------------------------------------------


async def delete(
        id: int,
        db: AsyncSession = Depends(get_async_db)):
    try:
        query = sql_delete(AbcModel).where(AbcModel.id == id)
        await db.execute(query)
        await db.commit()
    except exc.SQLAlchemyError as e:
        await db.rollback()
        print(f"Database error during creation: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while saving changes to the database.",
        )
    return None
