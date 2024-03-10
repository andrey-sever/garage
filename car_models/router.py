from fastapi import APIRouter
from car_models.dao import CarModelDAO
from car_models.shemas import SCarModel

router = APIRouter(
    prefix="/car_models",
    tags=["Модели автомобилей"],
)


@router.get("")
async def get_car_models() -> list[SCarModel]:
    return await CarModelDAO.find_all()
