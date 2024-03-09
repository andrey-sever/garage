from sqlalchemy import Column, Integer, String
from database import Base


class CarModels(Base):
    __tablename__ = 'car_models'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)