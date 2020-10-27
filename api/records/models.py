from django.db import models
import json
from django.utils.translation import gettext_lazy as _
from enum import Enum

class Excludions:
    CRATE = ('record_type', 'deadline', 'executor_info', 'done_criteria', 'done_plan')
    ARCHIVE = ()
    NOTE = ('record_type', 'deadline', 'executor_info', 'done_criteria', 'done_plan')
    AWAIT = ('record_type', 'done_criteria', 'done_plan')
    LATER = ('record_type', 'deadline', 'executor_info', 'done_criteria', 'done_plan')
    CALENDAR = ('record_type', 'executor_info', 'done_criteria', 'done_plan')
    PROJECT = ('record_type', 'deadline', 'executor_info')
    DONE = ()

class RecordTypes:
    CRATE = 'crate'
    ARCHIVE = 'archive'
    NOTE = 'note'
    AWAIT = 'await'
    LATER = 'later'
    CALENDAR = 'calendar'
    PROJECT = 'project'
    DONE = 'done'
class Record(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    creation_date = models.DateTimeField(
        auto_now_add=True, blank=True, db_column='creation_date')
    note = models.CharField(max_length=4096, db_column='note')
    record_type = models.CharField(max_length=16, db_column='record_type')
    root_id = models.IntegerField(db_column='root_id', default=None)
    deadline = models.DateTimeField(db_column='deadline', default=None)
    executor_info = models.CharField(max_length=4096, db_column='executor_info', default=None)
    done_criteria = models.CharField(max_length=4096, db_column='done_criteria', default=None)
    done_plan = models.CharField(max_length=4096, db_column='done_plan', default=None)

    def as_json(self):
        return {'id': self.id, 'creation_date': f'{self.creation_date}', 'note': self.note, 'record_type': self.record_type, 'root_id': self.root_id}

    class Meta:
        db_table = 'records'

