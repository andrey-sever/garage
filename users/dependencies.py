from datetime import datetime
from fastapi import Request, Depends
from jose import JWTError, jwt
from exeptions import *
from users.dao import UsersDAO
from config import settings
from users.models import Users
from users.roles import UserRole


def get_token(request: Request):
    token = request.cookies.get("garage_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        pyload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise IncorrectTokenFormatException
    expire: str = pyload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_id: str = pyload.get("sub")
    if not user_id:
        raise UserIsNotPresentException
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentException

    return user


async def get_current_admin_user(admin_user: Users = Depends(get_current_user)):
    if admin_user.role != UserRole.ADMIN:
        raise UserIsNotPresentException
    return admin_user
