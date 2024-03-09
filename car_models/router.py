from fastapi import APIRouter
from car_models.dao import CarModelDAO

router = APIRouter(
    prefix = "/car_models",
    tags = ["Модели автомобилей"],
)


@router.get("")
async def get_car_models():
    return await CarModelDAO.find_all()