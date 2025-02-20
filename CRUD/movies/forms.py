from django import forms
from .models import MovieInfo

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieInfo
        fields = ['title', 'desc', 'year','success']
