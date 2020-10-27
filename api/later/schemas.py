import records.models
from ninja import Schema
from pydantic_django import PydanticDjangoModel

class LaterRecordIn(PydanticDjangoModel):
    def get_object(self):
        o = records.models.Record()
        o.note = self.note
        o.root_id = self.root_id
        o.record_type = records.models.RecordTypes.LATER
        return o
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = (list(records.models.Excludions.IN_EXCLUDE) + list(records.models.Excludions.LATER))


class LaterRecordOut(PydanticDjangoModel):
    class Config:
        model = records.models.Record
        orm_mode = True
        exclude = (list(records.models.Excludions.OUT_EXCLUDE) + list(records.models.Excludions.ARCHIVE))