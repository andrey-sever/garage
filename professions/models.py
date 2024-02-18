from sqlalchemy import Column, Integer, String
from database import Base


class Professions(Base):
    __tablename__ = 'professions'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)