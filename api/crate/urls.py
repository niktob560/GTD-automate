from django.http import HttpResponseBadRequest
from ninja import NinjaAPI
import records.models
import records.schemas

from typing import List


api = NinjaAPI(urls_namespace='crate')


@api.post("/post_record")
def post_crate_record(request, r: records.schemas.RecordIn):
    try:
        if r.note.__len__() < 4:
            raise ValueError("Note must contain at least 4 chars")
        record = records.models.Record()
        record.note = r.note
        record.record_type = records.models.RecordTypes.CRATE
        record.save()
    except Exception as e:
        print(f"Failed to post record: {e}")
        return {'result': 'error', 'code': 1}
    else:
        return {'result': 'success', 'code': 0}


@api.get("/get_record", response=records.schemas.RecordOut)
def get_crate_record(request, id: int):
    try:
        if id <= 0:
            raise ValueError("Bad id")
        rs = records.models.Record.objects.filter(id=id)
        if rs.__len__() <= (id - 1):
            raise ValueError("Bad id")
        r = rs[0]
        return r
    except Exception as e:
        print(f"{e}")
        return HttpResponseBadRequest(content=f"{e}")


@api.get("/get_records", response=List[records.schemas.RecordOut])
def get_crate_records(request, limit: int = 100, offset: int = 0):
    if limit > 500:
        limit = 500
    return list(records.models.Record.objects.order_by('-id')[offset:(offset+limit)])


@api.delete("/delete_record")
def delete_crate_record(request, id: int):
    try:
        ret = records.models.Record.objects.filter(id=id).delete()
        if ret[0] == 0:
            raise ValueError('Deleted zero elements')
    except Exception as e:
        print(f"Failed to delete id{id}: {e}")
        return {'result': 'error', 'code': 1}
    else:
        return {'result': 'success', 'code': 0}
