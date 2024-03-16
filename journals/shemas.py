from pydantic import BaseModel
from datetime import datetime


class SJournals(BaseModel):
    data_exit: datetime
    data_entry: datetime
    id_car: int
    id_user: int

    class Config:
        # orm_mode = True
        from_attributes = True
