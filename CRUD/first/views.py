from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def print_welcome(request):
    return render(request,"first_index.html")