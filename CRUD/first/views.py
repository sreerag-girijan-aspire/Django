from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

movie_dict={
    "title":"Marco",
    "desc":"Adattu is one of the most renowned gold-trading families in Kerala. Unexpectedly, a mysterious incident shakes the Adattu family. George, the head of the family, sets out to uncover the truth and find those responsible. At the same time, his younger brother, Marco, embarks on the same quest but through a different Path. This forms the core of Marco, an intense Violent action-packed drama.",
    "year":"20 December 2024"
}
def print_welcome(request):
    return render(request,"first_index.html",movie_dict)