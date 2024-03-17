from fastapi import APIRouter, Depends
from journals.dao import JournalDAO
from journals.shemas import SJournals
from users.dependencies import get_current_user
from users.models import Users

router = APIRouter(
    prefix="/journals",
    tags=["Журнал"],
)


@router.get("")
async def get_journals(user: Users = Depends(get_current_user)) -> list[SJournals]:
    return await JournalDAO.find_all(id_user=user.id)


@router.post("/add")
async def add_journal(journal_data: SJournals):
    await JournalDAO.add(
        data_exit=journal_data.data_exit,
        data_entry=journal_data.data_entry,
        id_car=journal_data.id_car,
        id_user=journal_data.id_user
    )
