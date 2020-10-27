import records.schemas
import wait.models
from ninja import Schema
from pydantic_django import PydanticDjangoModel
from datetime import datetime, date, time


class AwaitRecordOut(PydanticDjangoModel):
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = records.models.Excludions.AWAIT

class AwaitRecordIn(records.schemas.RecordIn):
    deadline: datetime
    executor: str

class AwaitRecordFromCrate(Schema):
    deadline: datetime
    executor: str

class Deadline(Schema):
    deadline: datetime

class Executor(Schema):
    executor: str