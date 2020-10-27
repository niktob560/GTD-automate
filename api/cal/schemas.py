import records.schemas
import wait.models
from ninja import Schema
from pydantic_django import PydanticDjangoModel
from datetime import datetime, date, time


class CalendarRecordOut(PydanticDjangoModel):
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = (list(records.models.Excludions.OUT_EXCLUDE) + list(records.models.Excludions.CALENDAR))

class CalendarRecordIn(PydanticDjangoModel):
    deadline: datetime
    def get_object(self):
        o = records.models.Record()
        o.note = self.note
        o.root_id = self.root_id
        o.deadline = self.deadline
        o.record_type = records.models.RecordTypes.CALENDAR
        return o
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = (list(records.models.Excludions.IN_EXCLUDE) + list(records.models.Excludions.CALENDAR))

class CalendarRecordFromCrate(Schema):
    deadline: datetime

class Deadline(Schema):
    deadline: datetime