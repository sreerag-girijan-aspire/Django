from django.urls import path,include
from temptest import views
from temptest.views import ApiViewMovies,APIViewDelete,RegisterAPI,LoginAPI,MovieViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'viewset', MovieViewSet, basename='viewset')
urlpatterns = router.urls


urlpatterns=[
    path("",include(router.urls)),
    path("view/",views.movie_view,name="movie_view"),
    path("delete/<int:pk>/",views.delete,name="delete"),
    path("apimovies",ApiViewMovies.as_view(),name="apimovies"),
    path("movieinfo/<int:pk>/delete/",APIViewDelete.as_view(),name="movieinfodelete"),
    path("registerapi",RegisterAPI.as_view(),name="registerapi"),
    path("loginapi",LoginAPI.as_view(),name="loginapi")
]