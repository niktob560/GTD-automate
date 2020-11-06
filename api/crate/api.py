from django.http import HttpResponseBadRequest
from ninja import Router
import records.models
import crate.schemas
import wait.schemas
import wait.api

from typing import List
from datetime import datetime, timedelta, date

from security.api import AuthBearer

router = Router()


@router.post('/post_record', auth=AuthBearer())
def post_crate_record(request, r: crate.schemas.CrateRecordIn):
    try:
        if r.note.__len__() < 4:
            raise ValueError('Note must contain at least 4 chars')
        record = r.get_object()
        record.owner_token = request.auth.owner_token
        record.save()
    except Exception as e:
        print(f'Failed to post record: {e}')
        return {'result': 'error', 'code': 1}
    else:
        return {'result': 'success', 'code': 0}


@router.get('/get_record', response=crate.schemas.CrateRecordOut, auth=AuthBearer())
def get_crate_record(request, id: int):
    try:
        if id <= 0:
            raise ValueError('Bad id')
        rs = records.models.Record.objects.filter(
            id=id, record_type=records.models.RecordTypes.CRATE, owner_token=request.auth.owner_token)
        r = rs[0]
        return r
    except Exception as e:
        print(f'{e}')
        return HttpResponseBadRequest(content=f'{e}')


@router.get('/get_records', response=List[crate.schemas.CrateRecordOut], auth=AuthBearer())
def get_crate_records(request, limit: int = 100, offset: int = 0):
    if limit > 500:
        limit = 500
    if offset < 0:
        offset = 0
    return list(records.models.Record.objects.filter(record_type=records.models.RecordTypes.CRATE, owner_token=request.auth.owner_token).order_by('-id')[offset:(offset+limit)])


@router.delete('/delete_record', auth=AuthBearer())
def delete_crate_record(request, id: int):
    try:
        ret = records.models.Record.objects.filter(
            id=id, record_type=records.models.RecordTypes.CRATE, owner_token=request.auth.owner_token).delete()
        if ret[0] == 0:
            raise ValueError('Deleted zero elements')
    except Exception as e:
        print(f'Failed to delete id{id}: {e}')
        return {'result': 'error', 'code': 1}
    else:
        return {'result': 'success', 'code': 0}
