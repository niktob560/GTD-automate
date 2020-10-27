import records.models
from ninja import Schema
from pydantic_django import PydanticDjangoModel

class RecordIn(PydanticDjangoModel):
    def get_object(self):
        o = records.models.Record()
        o.note = self.note
        o.root_id = self.root_id
        o.deadline = self.deadline
        o.executor_info = self.executor
        o.done_criteria = self.done_criteria
        o.done_plan = self.done_plan
        return o
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = records.models.Excludions.IN_EXCLUDE


class RecordOut(PydanticDjangoModel):
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = records.models.Excludions.OUT_EXCLUDE
