from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request,"create.html")

def edit(request):
    return render(request,"edit.html")

movie_dict={
    "movies":[{
    "title":"Marco",
    "desc":"Adattu is one of the most renowned gold-trading families in Kerala. Unexpectedly, a mysterious incident shakes the Adattu family. George, the head of the family, sets out to uncover the truth and find those responsible. At the same time, his younger brother, Marco, embarks on the same quest but through a different Path. This forms the core of Marco, an intense Violent action-packed drama.",
    "year":"20 December 2024",
    "success":True,
    "img":"Marco.jpeg",
    },
    {
    "title":"Pushpa 2 - The Rule",
    "desc":"Pushpa: The Rule—Part 2 is a Telugu movie written and directed by Sukumar Bandreddi. It stars Allu Arjun, Rashmika Mandanna, and Fahadh Faasil in prominent roles. The Rule begins on 5th December 2024.",
    "year":"5 December 2024",
    "success":True,
    "img":"Pushpa2.avif",
    },
    {
    "title":"Bromance",
    "desc":"Binto teams up with his brother`s friends for a thrilling adventure to find him, leading to unexpected twists, discoveries, and unforgettable moments.",
    "year":"14 February 2025",
    "success":True,
    "img":"Bromance.avif",
    }
              ]
}
def list(request):
    return render(request,"list.html",movie_dict)