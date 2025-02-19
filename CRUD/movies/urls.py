from django.urls import path
from . import views

urlpatterns=[
    path("create/",views.create),
    path("edit/",views.edit),
    path("list/",views.list)
]