from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from database import Base
from users.roles import UserRole


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.USER)
    email = Column(String(100), nullable=False)
    profession_id = Column(ForeignKey('professions.id'), nullable=False)
    password = Column(String(60), nullable=False)

