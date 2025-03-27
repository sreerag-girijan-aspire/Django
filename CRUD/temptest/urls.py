from django.urls import path,include
# from rest_framework.routers import DefaultRouter
# from .views import MovieViewSet
from . import views


# router = DefaultRouter()
# router.register(r'movieviewset', MovieViewSet)

urlpatterns=[
    path('set-cookie/', views.set_cookie, name='set_cookie'),
    path('get-cookie/', views.get_cookie, name='get_cookie'),
    path('delete-cookie/', views.delete_cookie, name='delete_cookie'),
    path('set_session/', views.set_session, name='set_session'),
    path('get_session/', views.get_session, name='get_session'),
    path('delete_session/', views.delete_session, name='delete_session'),
    path("custom/",views.custom_tag,name="custom"),
    # path('', include(router.urls)),
]