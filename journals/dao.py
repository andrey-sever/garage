from dao.base import BaseDAO
from journals.models import Journals


class JournalDAO(BaseDAO):
    model = Journals
