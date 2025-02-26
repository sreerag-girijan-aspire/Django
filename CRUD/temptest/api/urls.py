from django.urls import path
from temptest import views
urlpatterns=[
    path("index/",views.index,name="index")
]