from ninja import Schema
import crate.models
from pydantic_django import PydanticDjangoModel


class CrateRecordIn(Schema):
    note: str

class CrateRecordId(Schema):
    id: int

class CrateRecordOut(PydanticDjangoModel):
    class Config:
        model = crate.models.CrateRecord
        orm_mode = True
    # note: str
    # creation_date: str
    # id: int