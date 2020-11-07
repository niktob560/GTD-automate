from django.http import HttpResponseBadRequest
from ninja import Router
import records.models
import projects.schemas

from typing import List

from security.api import AuthBearer

from crate.api import post_crate_record
import records.models

router = Router()


@router.post('/post_record', auth=AuthBearer())
def post_projects_record(request, r: projects.schemas.ProjectRecordIn):
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


@router.get('/get_record', response=projects.schemas.ProjectRecordOut, auth=AuthBearer())
def get_projects_record(request, id: int):
    try:
        if id <= 0:
            raise ValueError('Bad id')
        rs = records.models.Record.objects.filter(
            id=id, record_type=records.models.RecordTypes.PROJECT, owner_token=request.auth.owner_token)
        r = rs[0]
        return r
    except Exception as e:
        print(f'{e}')
        return HttpResponseBadRequest(content=f'{e}')


@router.get('/get_records', response=List[projects.schemas.ProjectRecordOut], auth=AuthBearer())
def get_projects_records(request, limit: int = 100, offset: int = 0):
    if limit > 500:
        limit = 500
    if offset < 0:
        offset = 0
    l = list(records.models.Record.objects.filter(record_type=records.models.RecordTypes.PROJECT, owner_token=request.auth.owner_token).order_by('-id')[offset:(offset+limit)])
    for i in l:
        print(i.as_json())
    return l


@router.delete('/delete_record', auth=AuthBearer())
def delete_projects_record(request, id: int):
    try:
        ret = records.models.Record.objects.filter(
            id=id, record_type=records.models.RecordTypes.PROJECT, owner_token=request.auth.owner_token).delete()
        if ret[0] == 0:
            raise ValueError('Deleted zero elements')
    except ValueError as e:
        return {'result': 'error', 'code': 1, 'info': f'{e}'}
    except Exception as e:
        print(f'Failed to delete id {id}: {e}')
        return {'result': 'error', 'code': 2}
    else:
        return {'result': 'success', 'code': 0}


@router.patch('/update_done_criteria', auth=AuthBearer())
def update_done_criteria(request, record_id: int, new_done: projects.schemas.DoneCriteria):
    try:
        if record_id <= 0:
            raise ValueError('Bad id')
        ret = records.models.Record.objects.filter(
            id=record_id, record_type=records.models.RecordTypes.PROJECT, owner_token=request.auth.owner_token).update(done_criteria=new_done.criteria)
        if ret == 0:
            raise ValueError('Updated zero elements')
    except ValueError as e:
        return {'result': 'error', 'code': 1, 'info': f'{e}'}
    except Exception as e:
        print(f'Failed to update criteria id {id}: {e}')
        return {'result': 'error', 'code': 2}
    else:
        return {'result': 'success', 'code': 0}


@router.patch('/update_done_pan', auth=AuthBearer())
def update_done_pan(request, record_id: int, new_done: projects.schemas.DonePlan):
    try:
        if record_id <= 0:
            raise ValueError('Bad id')
        ret = records.models.Record.objects.filter(
            id=record_id, record_type=records.models.RecordTypes.PROJECT, owner_token=request.auth.owner_token).update(done_plan=new_done.plan)
        if ret == 0:
            raise ValueError('Updated zero elements')
    except ValueError as e:
        return {'result': 'error', 'code': 1, 'info': f'{e}'}
    except Exception as e:
        print(f'Failed to update plan id {id}: {e}')
        return {'result': 'error', 'code': 2}
    else:
        return {'result': 'success', 'code': 0}


@router.patch('/update_note', auth=AuthBearer())
def update_note(request, record_id: int, new_note: projects.schemas.Note):
    try:
        if record_id <= 0:
            raise ValueError('Bad id')
        ret = records.models.Record.objects.filter(
            id=record_id, record_type=records.models.RecordTypes.PROJECT, owner_token=request.auth.owner_token).update(note=new_note.note)
        if ret == 0:
            raise ValueError('Updated zero elements')
    except ValueError as e:
        return {'result': 'error', 'code': 1, 'info': f'{e}'}
    except Exception as e:
        print(f'Failed to note id {id}: {e}')
        return {'result': 'error', 'code': 2}
    else:
        return {'result': 'success', 'code': 0}


@router.patch('/make_project', auth=AuthBearer())
def aprojects_crate_record(request, id: int, additional: projects.schemas.ProjectRecordFromCrate):
    try:
        r = records.models.Record.objects.filter(
            id=id, owner_token=request.auth.owner_token)
        if not r:
            raise ValueError('No such record')
        if r[0].record_type == records.models.RecordTypes.PROJECT:
            raise ValueError('Already a project record')
        for i in additional.steps:
            if i.__len__() < 4:
                raise ValueError('Step must contain at least 4 chars')
        for i in additional.steps:
            record = records.models.Record()
            record.note = i
            record.root_id = id
            record.owner_token = request.auth.owner_token
            record.record_type = records.models.RecordTypes.CRATE
            record.save()
        r.update(record_type=records.models.RecordTypes.PROJECT,
                 deadline=additional.deadline, 
                 done_plan=additional.done_plan,
                 done_criteria=additional.done_criteria)
    except ValueError as e:
        return {'result': 'error', 'code': 1, 'info': f'{e}'}
    except Exception as e:
        print(f'Failed to make project id {id}: {e}')
        return {'result': 'error', 'code': 2}
    else:
        return {'result': 'success', 'code': 0}
