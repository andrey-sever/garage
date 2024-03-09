from dao.base import BaseDAO
from professions.models import Professions


class ProfessionDAO(BaseDAO):
    model = Professions
