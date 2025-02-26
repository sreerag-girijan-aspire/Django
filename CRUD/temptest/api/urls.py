from django.urls import path
from temptest import views
urlpatterns=[
    path("view/",views.movie_view,name="movie_view"),
    path("delete/<int:pk>/",views.delete,name="delete")
]