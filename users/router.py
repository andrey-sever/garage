from fastapi import APIRouter, HTTPException, status, Response
from users.auth import get_password_hash, authenticate_user, create_access_token
from users.dao import UsersDAO
from users.shemas import SUserRegister, SUserAuth

router = APIRouter(
    prefix="/auth",
    tags=["Идентификация пользователя"],
)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await UsersDAO.find_one_for_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь существует")
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(name=user_data.name, email=user_data.email,
                       profession_id=user_data.profession_id, password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": user.id})
    response.set_cookie("garage_access_token", access_token, httponly=True)
    return access_token
