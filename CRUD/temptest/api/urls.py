from django.urls import path
from temptest import views
urlpatterns=[
    path("index/",views.index,name="index"),
    path("view",views.movie_view,name="movie_view"),
]