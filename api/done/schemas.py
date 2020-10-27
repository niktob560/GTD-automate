import records.models
from ninja import Schema
from pydantic_django import PydanticDjangoModel

class DoneRecordIn(Schema):
    note: str


class DoneRecordOut(PydanticDjangoModel):
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = records.models.Excludions.DONE