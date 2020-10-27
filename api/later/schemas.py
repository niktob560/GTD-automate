import records.models
from ninja import Schema
from pydantic_django import PydanticDjangoModel

class LaterRecordIn(Schema):
    note: str


class LaterRecordOut(PydanticDjangoModel):
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = ('record_type')