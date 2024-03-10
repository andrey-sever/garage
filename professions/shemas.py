from pydantic import BaseModel


class SProfession(BaseModel):
    id: int
    name: str

    class Config:
        # orm_mode = True
        from_attributes = True
