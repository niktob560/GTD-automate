from django.http import HttpResponseBadRequest
from ninja import Router
import records.models
import archive.schemas

from typing import List

from security.api import AuthBearer

router = Router()

@router.post('/post_record', auth=AuthBearer())
def post_archive_record(request, r: archive.schemas.ArchiveRecordIn):
    try:
        if r.note.__len__() < 4:
            raise ValueError('Note must contain at least 4 chars')
        record = r.get_object()
        record.owner_token = request.auth.owner_token
        record.save()
    except ValueError as e:
        return {'result': 'error', 'code': 1, 'info': f'{e}'}
    except Exception as e:
        print(f'Failed to post record: {e}')
        return {'result': 'error', 'code': 2}
    else:
        return {'result': 'success', 'code': 0}


@router.get('/get_record', response=archive.schemas.ArchiveRecordOut, auth=AuthBearer())
def get_archive_record(request, id: int):
    try:
        if id <= 0:
            raise ValueError('Bad id')
        rs = records.models.Record.objects.filter(
            id=id, record_type=records.models.RecordTypes.ARCHIVE, owner_token=request.auth.owner_token)
        r = rs[0]
        return r
    except Exception as e:
        print(f'{e}')
        return HttpResponseBadRequest(content=f'{e}')


@router.get('/get_records', response=List[archive.schemas.ArchiveRecordOut], auth=AuthBearer())
def get_archive_records(request, limit: int = 100, offset: int = 0):
    if limit > 500:
        limit = 500
    if offset < 0:
        offset = 0
    return list(records.models.Record.objects.filter(record_type=records.models.RecordTypes.ARCHIVE, owner_token=request.auth.owner_token).order_by('-id')[offset:(offset+limit)])


@router.delete('/delete_record', auth=AuthBearer())
def delete_archive_record(request, id: int):
    try:
        ret = records.models.Record.objects.filter(id=id, record_type=records.models.RecordTypes.ARCHIVE, owner_token=request.auth.owner_token).delete()
        if ret[0] == 0:
            raise ValueError('Deleted zero elements')
    except ValueError as e:
        return {'result': 'error', 'code': 1, 'info': f'{e}'}
    except Exception as e:
        print(f'Failed to delete id{id}: {e}')
        return {'result': 'error', 'code': 2}
    else:
        return {'result': 'success', 'code': 0}


@router.patch('/make_archive', auth=AuthBearer())
def archive_crate_record(request, id: int, new_note: records.schemas.Note = None):
    try:
        if id <= 0:
            raise ValueError('Bad id')
        if new_note:
            ret = records.models.Record.objects.filter(
                id=id, owner_token=request.auth.owner_token).update(record_type=records.models.RecordTypes.ARCHIVE, note=new_note.note)
        else:
            ret = records.models.Record.objects.filter(
                id=id, owner_token=request.auth.owner_token).update(record_type=records.models.RecordTypes.ARCHIVE)
        if ret == 0:
            raise ValueError('Changed zero elements')
    except ValueError as e:
        return {'result': 'error', 'code': 1, 'info': f'{e}'}
    except Exception as e:
        print(f'Failed to archive id{id}: {e}')
        return {'result': 'error', 'code': 2}
    else:
        return {'result': 'success', 'code': 0}

@router.patch('/update_note', auth=AuthBearer())
def update_note(request, record_id: int, new_note: records.schemas.Note):
    try:
        if record_id <= 0:
            raise ValueError('Bad id')
        ret = records.models.Record.objects.filter(
            id=record_id, record_type=records.models.RecordTypes.ARCHIVE, owner_token=request.auth.owner_token).update(note=new_note.note)
        if ret == 0:
            raise ValueError('Updated zero elements')
    except ValueError as e:
        return {'result': 'error', 'code': 1, 'info': f'{e}'}
    except Exception as e:
        print(f'Failed to note id {id}: {e}')
        return {'result': 'error', 'code': 2}
    else:
        return {'result': 'success', 'code': 0}