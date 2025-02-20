from django.urls import path
from . import views

urlpatterns=[
    path("create/",views.create,name='create'),
    path("edit/",views.edit,name='edit'),
    path("list/",views.list,name='list'),
    path('movieform/', views.MovieCreateView.as_view(), name='movie_form_create'),
    path("movieformupdate/<int:pk>/",views.MovieUpdateView.as_view(),name='movie_form_update'),
    path("movieformdelete/<int:pk>/",views.MovieDeleteView.as_view(),name="movie_form_delete"),
]