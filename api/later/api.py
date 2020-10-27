from django.http import HttpResponseBadRequest
from ninja import Router
import records.models
import later.schemas

from typing import List

router = Router()

@router.post('/post_record')
def post_later_record(request, r: later.schemas.LaterRecordIn):
    try:
        if r.note.__len__() < 4:
            raise ValueError('Note must contain at least 4 chars')
        record = r.get_object()
        record.save()
    except Exception as e:
        print(f'Failed to post record: {e}')
        return {'result': 'error', 'code': 1}
    else:
        return {'result': 'success', 'code': 0}


@router.get('/get_record', response=later.schemas.LaterRecordOut)
def get_later_record(request, id: int):
    try:
        if id <= 0:
            raise ValueError('Bad id')
        rs = records.models.Record.objects.filter(
            id=id, record_type=records.models.RecordTypes.LATER)
        r = rs[0]
        return r
    except Exception as e:
        print(f'{e}')
        return HttpResponseBadRequest(content=f'{e}')


@router.get('/get_records', response=List[later.schemas.LaterRecordOut])
def get_later_records(request, limit: int = 100, offset: int = 0):
    if limit > 500:
        limit = 500
    if offset < 0:
        offset = 0
    return list(records.models.Record.objects.filter(record_type=records.models.RecordTypes.LATER).order_by('-id')[offset:(offset+limit)])


@router.delete('/delete_record')
def delete_later_record(request, id: int):
    try:
        ret = records.models.Record.objects.filter(id=id, record_type=records.models.RecordTypes.LATER).delete()
        if ret[0] == 0:
            raise ValueError('Deleted zero elements')
    except Exception as e:
        print(f'Failed to delete id {id}: {e}')
        return {'result': 'error', 'code': 1}
    else:
        return {'result': 'success', 'code': 0}

@router.patch('/make_later')
def later_crate_record(request, id: int):
    try:
        if id <= 0:
            raise ValueError('Bad id')
        ret = records.models.Record.objects.filter(
            id=id).update(record_type=records.models.RecordTypes.LATER)
        print(ret)
        if ret == 0:
            raise ValueError('Changed zero elements')
    except Exception as e:
        print(f'Failed to later id{id}: {e}')
        return {'result': 'error', 'code': 1}
    else:
        return {'result': 'success', 'code': 0}