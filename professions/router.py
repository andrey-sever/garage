from fastapi import APIRouter


router = APIRouter(
    prefix="/professions",
    tags=["Профессии"],
)


@router.get("")
def get_professions():
    pass

@router.get("/{profession_id}")
def get_profession(profession_id):
    pass