from fastapi import APIRouter, HTTPException

from users.auth import get_password_hash
from users.dao import UsersDAO
from users.shemas import SUserRegister

router = APIRouter(
    prefix="/auth",
    tags=["Идентификация пользователя"],
)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await UsersDAO.find_one_for_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=422, detail="Пользователь существует")
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(name=user_data.name, email=user_data.email,
                       profession_id=user_data.profession_id, password=hashed_password)
