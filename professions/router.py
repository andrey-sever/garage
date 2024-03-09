from fastapi import APIRouter
from professions.dao import ProfessionDAO

router = APIRouter(
    prefix="/professions",
    tags=["Профессии"],
)


@router.get("")
async def get_professions():
    return await ProfessionDAO.find_all()

@router.get("/{profession_id}")
def get_profession(profession_id):
    pass