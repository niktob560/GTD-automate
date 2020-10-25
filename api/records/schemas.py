import records.models
from ninja import Schema
from pydantic_django import PydanticDjangoModel

class RecordIn(Schema):
    note: str


class RecordOut(PydanticDjangoModel):
    class Config:
        model = records.models.Record
        orm_mode = True