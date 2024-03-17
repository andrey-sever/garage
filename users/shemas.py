from pydantic import BaseModel, EmailStr
from users.roles import UserRole


class SUserRegister(BaseModel):
    # id:
    name: str
    role: UserRole
    email: EmailStr
    profession_id: int
    password: str

    class Config:
        # orm_mode = True
        from_attributes = True


class SUserAuth(BaseModel):
    # id:
    email: EmailStr
    password: str

    class Config:
        # orm_mode = True
        from_attributes = True
