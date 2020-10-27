from django.http import HttpResponseBadRequest
from ninja import Router
import records.models
import done.schemas

from typing import List

router = Router()

@router.post('/post_record')
def post_done_record(request, r: done.schemas.DoneRecordIn):
    try:
        if r.done.__len__() < 4:
            raise ValueError('Note must contain at least 4 chars')
        record = records.models.Record()
        record.done = r.done
        record.record_type = records.models.RecordTypes.DONE
        record.save()
    except Exception as e:
        print(f'Failed to post record: {e}')
        return {'result': 'error', 'code': 1}
    else:
        return {'result': 'success', 'code': 0}


@router.get('/get_record', response=done.schemas.DoneRecordOut)
def get_done_record(request, id: int):
    try:
        if id <= 0:
            raise ValueError('Bad id')
        rs = records.models.Record.objects.filter(
            id=id, record_type=records.models.RecordTypes.DONE)
        r = rs[0]
        return r
    except Exception as e:
        print(f'{e}')
        return HttpResponseBadRequest(content=f'{e}')


@router.get('/get_records', response=List[done.schemas.DoneRecordOut])
def get_done_records(request, limit: int = 100, offset: int = 0):
    if limit > 500:
        limit = 500
    if offset < 0:
        offset = 0
    return list(records.models.Record.objects.filter(record_type=records.models.RecordTypes.DONE).order_by('-id')[offset:(offset+limit)])


@router.delete('/delete_record')
def delete_done_record(request, id: int):
    try:
        ret = records.models.Record.objects.filter(id=id, record_type=records.models.RecordTypes.DONE).delete()
        if ret[0] == 0:
            raise ValueError('Deleted zero elements')
    except Exception as e:
        print(f'Failed to delete id{id}: {e}')
        return {'result': 'error', 'code': 1}
    else:
        return {'result': 'success', 'code': 0}

@router.patch('/make_done')
def done_crate_record(request, id: int):
    try:
        if id <= 0:
            raise ValueError('Bad id')
        ret = records.models.Record.objects.filter(
            id=id).update(record_type=records.models.RecordTypes.DONE)
        print(ret)
        if ret == 0:
            raise ValueError('Changed zero elements')
    except Exception as e:
        print(f'Failed to done id{id}: {e}')
        return {'result': 'error', 'code': 1}
    else:
        return {'result': 'success', 'code': 0}