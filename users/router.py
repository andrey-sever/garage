from fastapi import APIRouter, Response, Depends
from exeptions import *
from users.auth import get_password_hash, authenticate_user, create_access_token
from users.dao import UsersDAO
from users.dependencies import get_current_user, get_current_admin_user
from users.models import Users
from users.shemas import SUserRegister, SUserAuth

router = APIRouter(
    prefix="/auth",
    tags=["Идентификация пользователя"],
)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await UsersDAO.find_one_for_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(name=user_data.name, email=user_data.email,
                       profession_id=user_data.profession_id, password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("garage_access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("garage_access_token")


@router.get("/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user


@router.get("/all")
async def users_all(current_user: Users = Depends(get_current_admin_user)):
    return await UsersDAO.find_all()
