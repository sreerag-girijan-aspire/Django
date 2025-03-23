from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.custom_logout_view, name='custom_logout'),
    path('register/', views.register, name='register'),

    path("create/",views.create,name='create'),
    path("edit/",views.edit,name='edit'),
    path("list/",views.list,name='list'),
    path('movieformcreate/', views.MovieCreateView.as_view(), name='movie_form_create'),
    path("movieformupdate/<int:pk>/",views.MovieUpdateView.as_view(),name='movie_form_update'),
    path("movieformdelete/<int:pk>/",views.MovieDeleteView.as_view(),name="movie_form_delete"),
    path("movieformlist/",views.MovieFormView.as_view(),name="movie_form_list"),
    path("",views.MovieFormView.as_view(),name="movie_form_list"),
    path("header/",views.view_headers,name="view_headers"),
    path("customheader/",views.view_custom_header,name="custom_header"),
    path("querystring/",views.query_string,name="query_string"),
    path("success/",views.success,name="success"),
]