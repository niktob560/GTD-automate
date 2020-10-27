import records.models
from ninja import Schema
from pydantic_django import PydanticDjangoModel

class DoneRecordIn(PydanticDjangoModel):
    def get_object(self):
        o = records.models.Record()
        o.note = self.note
        o.root_id = self.root_id
        o.deadline = self.deadline
        o.executor_info = self.executor_info
        o.done_criteria = self.done_criteria
        o.done_plan = self.done_plan
        o.record_type = records.models.RecordTypes.DONE
        return o
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = (list(records.models.Excludions.IN_EXCLUDE) + list(records.models.Excludions.DONE))


class DoneRecordOut(PydanticDjangoModel):
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = (list(records.models.Excludions.OUT_EXCLUDE) + list(records.models.Excludions.DONE))