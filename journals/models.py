from sqlalchemy import Column, Integer, DateTime, ForeignKey
from database import Base


class Journals(Base):
    __tablename__ = 'journals'

    id = Column(Integer, primary_key=True)
    data_exit = Column(DateTime)
    data_entry = Column(DateTime)
    id_car = Column(ForeignKey('cars.id'), nullable=False)
    id_user = Column(ForeignKey('users.id'), nullable=False)
