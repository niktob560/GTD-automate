import records.models
from ninja import Schema
from pydantic_django import PydanticDjangoModel

class CrateRecordIn(Schema):
    note: str


class CrateRecordOut(PydanticDjangoModel):
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = ('record_type')