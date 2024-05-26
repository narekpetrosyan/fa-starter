from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.crud.users import get_all_users, create_user
from core.models import db_helper
from core.schemas.user import UserRead, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=list[UserRead])
async def get_users(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    users = await get_all_users(session=session)
    return users


@router.post("/", response_model=UserRead)
async def create_user_post(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        user_create: UserCreate
):
    print(user_create)
    user = await create_user(session=session, user_create=user_create)
    return user
