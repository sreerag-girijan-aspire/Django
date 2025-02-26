from rest_framework import serializers
from movies.models import MovieInfo

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=MovieInfo
        fields="__all__"