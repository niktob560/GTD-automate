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

class AwaitRecordIn(PydanticDjangoModel):
    deadline: datetime
    executor_info: str
    def get_object(self):
        o = records.models.Record()
        o.note = self.note
        o.root_id = self.root_id
        o.deadline = self.deadline
        o.executor_info = self.executor_info
        o.record_type = records.models.RecordTypes.AWAIT
        return o
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = (list(records.models.Excludions.IN_EXCLUDE) + list(records.models.Excludions.AWAIT))

class AwaitRecordFromCrate(Schema):
    deadline: datetime
    executor: str

class Deadline(Schema):
    deadline: datetime

class Executor(Schema):
    executor: str