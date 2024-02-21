from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    profession_id = Column(ForeignKey('professions.id'), nullable=False)
    password = Column(String(60), nullable=False)

