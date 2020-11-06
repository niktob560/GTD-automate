from django.http import HttpResponseBadRequest
from ninja import Router
import records.models
import security.models
import security.schemas
import secrets
from datetime import datetime, timedelta


from typing import List
from datetime import datetime, timedelta, date

def generate_token(len=4096):
    alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890&*^%$'
    chars=[]
    for i in range(len):
        chars.append(secrets.choice(alphabet))
    return "".join(chars)

def get_expiration_datetime():
    return datetime.now() + timedelta(days=1)


router = Router()


@router.post('/login')
def login(request, lt: security.schemas.TokenIn):
    try:
        q = security.models.LongToken.objects.filter(token=lt.token)
        if q.__len__() != 1:
            raise ValueError("No such token")
        q = q.first()
        lt = lt.get_object()
        lt.id = q.id
        et = security.models.ExpiringToken()
        et.owner_token_id = lt
        et.token = generate_token()
        et.expire_at = get_expiration_datetime()
        t = et.token
        et.save()
    except Exception as e:
        print(f'Failed to login: {e}')
        return {'result': 'error', 'code': 1}
    else:
        return {'result': 'success', 'code': 0, 'token': t}