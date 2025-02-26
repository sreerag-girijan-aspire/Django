from django.urls import path
from temptest import views
from temptest.views import ApiViewMovies
urlpatterns=[
    path("view/",views.movie_view,name="movie_view"),
    path("delete/<int:pk>/",views.delete,name="delete"),
    path("apimovies",ApiViewMovies.as_view(),name="apimovies"),
]