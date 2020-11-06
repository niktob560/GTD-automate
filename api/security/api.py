from django.http import HttpResponseBadRequest
from ninja import Router
from ninja.security import HttpBearer
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


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        et = security.models.ExpiringToken.objects.filter(token=token, expire_at__gt = datetime.now())
        if et and et.__len__() == 1:
            return et.first()


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
        et.owner_token = lt
        et.token = generate_token()
        et.expire_at = get_expiration_datetime()
        t = et.token
        et.save()
    except Exception as e:
        print(f'Failed to login: {e}')
        return {'result': 'error', 'code': 1}
    else:
        return {'result': 'success', 'code': 0, 'token': t, 'expire_at': et.expire_at.strftime("%Y-%m-%d %H:%M:%S")}

@router.get('/test', auth=AuthBearer())
def test(request):
    return {'result': 'success', 'code': 0}