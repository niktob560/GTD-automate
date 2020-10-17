"""gtd_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponseBadRequest
from ninja import NinjaAPI
from typing import List
import crate.models
import crate.schemes
from django.http import HttpResponse


api = NinjaAPI()


@api.post("/crate/post_record")
def post_crate_record(request, note: crate.schemes.CrateRecordIn):
    try:
        record = crate.models.CrateRecord()
        record.note = note
        record.save()
        return {'result': 'success', 'code': 0}
    except Exception as e:
        print(f"{e}")
        return {'result': 'error', 'code': 1}

@api.get("/crate/get_record", response=crate.schemes.CrateRecordOut)
def get_crate_record(request, id: crate.schemes.CrateRecordIn):
    try:
        if id <= 0:
            raise ValueError("Bad id")
        rs = crate.models.CrateRecord.objects.filter(id=id)
        if rs.__len__() <= (id - 1):
            raise ValueError("Bad id")
        r = rs[0]
        return r
    except Exception as e:
        print(f"{e}")
        return HttpResponseBadRequest(content=f"{e}")
    
@api.get("/crate/get_records", response=List[crate.schemes.CrateRecordOut])
def get_crate_records(request):
    return list(crate.models.CrateRecord.objects.all())

@api.delete("/crate/delete_record")
def delete_crate_record(request, id: crate.schemes.CrateRecordId):
    pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
