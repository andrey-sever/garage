from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Cars(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    car_model_id = Column(ForeignKey('car_models.id'), nullable=False)
    number = Column(String(9), nullable=False)