from fastapi import APIRouter
from professions.dao import ProfessionDAO
from professions.shemas import SProfession

router = APIRouter(
    prefix="/professions",
    tags=["Профессии"],
)


@router.get("")
async def get_professions() -> list[SProfession]:
    return await ProfessionDAO.find_all()


@router.get("/{profession_id}")
def get_profession(profession_id):
    pass
