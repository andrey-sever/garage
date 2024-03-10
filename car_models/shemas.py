from pydantic import BaseModel


class SCarModel(BaseModel):
    id: int
    name: str

    class Config:
        # orm_mode = True
        from_attributes = True
