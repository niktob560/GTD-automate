import records.schemas
import projects.models
from ninja import Schema
from pydantic_django import PydanticDjangoModel
from datetime import datetime, date, time
from typing import List


class PlanRecord(PydanticDjangoModel):
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = ('owner_token',)

class ProjectRecordOut(PydanticDjangoModel):
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = (list(records.models.Excludions.OUT_EXCLUDE) + list(records.models.Excludions.PROJECT))

class ProjectRecordIn(PydanticDjangoModel):
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
    deadline: datetime
    steps: List[str]

class DoneCriteria(Schema):
    criteria: str

class DonePlan(Schema):
    plan: str

class Note(Schema):
    note: str