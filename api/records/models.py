from django.db import models
import json
from django.utils.translation import gettext_lazy as _
from enum import Enum

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
    id = models.AutoField(primary_key=True, db_column='id')
    creation_date = models.DateTimeField(
        auto_now_add=True, blank=True, db_column='creation_date')
    note = models.CharField(max_length=4096, db_column='note', name='note')
    record_type = models.CharField(max_length=16, db_column='record_type', name='record_type')

    def as_json(self):
        return {'id': self.id, 'creation_date': f'{self.creation_date}', 'note': self.note, 'record_type': self.record_type}

    class Meta:
        db_table = 'records'

