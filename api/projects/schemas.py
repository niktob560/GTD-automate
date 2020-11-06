import records.schemas
import wait.models
from ninja import Schema
from pydantic_django import PydanticDjangoModel
from datetime import datetime, date, time



class ProjectRecordOut(PydanticDjangoModel):
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = (list(records.models.Excludions.OUT_EXCLUDE) + list(records.models.Excludions.PROJECT))

class ProjectRecordIn(PydanticDjangoModel):
    done_criteria: str
    done_plan: str
    def get_object(self):
        o = records.models.Record()
        o.note = self.note
        o.root_id = self.root_id
        o.done_criteria = self.done_criteria
        o.done_plan = self.done_plan
        o.record_type = records.models.RecordTypes.PROJECT
        return o
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = (list(records.models.Excludions.IN_EXCLUDE) + list(records.models.Excludions.PROJECT))

class ProjectRecordFromCrate(Schema):
    done_criteria: str
    done_plan: str
    steps_ids: list(int)

class DoneCriteria(Schema):
    deadline: datetime

class DonePlan(Schema):
    executor: str