from django.db import models

class LongToken(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    token = models.CharField(max_length=1024, db_column='token')

    def as_json(self):
        return {'id': self.id, 'token': self.token}

    class Meta:
        db_table = 'long_tokens'

class ExpiringToken(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    token = models.CharField(max_length=4096, db_column='token')
    expire_at = models.DateTimeField(db_column='expire_at', auto_now_add=True, blank=True)
    owner_token_id = models.ForeignKey(LongToken, on_delete=models.CASCADE, db_column='owner_token_id')

    def as_json(self):
        return {'id': self.id, 'token': self.token, 'expire_at': self.expire_at, 'owner_token_id': self.owner_token_id}

    class Meta:
        db_table = 'expiring_tokens'