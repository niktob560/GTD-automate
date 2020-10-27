import records.models
from ninja import Schema
from pydantic_django import PydanticDjangoModel

class NotesRecordIn(Schema):
    note: str


class NotesRecordOut(PydanticDjangoModel):
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = ('record_type')