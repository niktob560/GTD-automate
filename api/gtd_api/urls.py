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
from django.http import HttpResponse

from crate.api import router as crate_router
from archive.api import router as archive_router


api = NinjaAPI()
api.add_router('/crate/', crate_router)
api.add_router('/archive/', archive_router)

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
