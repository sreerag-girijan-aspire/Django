from django.contrib import admin
from . models import MovieInfo,DirectorInfo,Actor
# Register your models here.
admin.site.register(MovieInfo)
admin.site.register(DirectorInfo)
admin.site.register(Actor)