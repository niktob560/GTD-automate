from django.db import models

# Create your models here.

class CrateRecord(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, db_column='creation_date')
    note = models.CharField(max_length=4096, db_column='note', name='note')
    def as_json(self):
        return {'id': self.id, 'creation_date': f"{self.creation_date}", 'note': self.note}
    class Meta:
        db_table = 'crate'