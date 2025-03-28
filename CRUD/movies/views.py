from django.shortcuts import render,redirect
from .models import MovieInfo
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView
from .forms import MovieForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout




def custom_logout_view(request):
    logout(request)  # This will log the user out
    return redirect('login')  # Redirect the user to a different page

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created!')
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



# Create your views here.
def create(request):
    if request.POST:
        print(request.POST)
        title=request.POST.get("title")
        desc=request.POST.get("desc")
        year=request.POST.get("year")
        success=request.POST.get("success")
        movie_obj=MovieInfo(title=title,desc=desc,year=year,success=success)
        movie_obj.save()
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


class MovieCreateView(LoginRequiredMixin,CreateView):
    model = MovieInfo
    form_class = MovieForm
    template_name = 'movie_form.html'
    success_url = '/success/'  # Where to redirect after successful form submission

    
class MovieUpdateView(LoginRequiredMixin,UpdateView):
    model=MovieInfo
    form_class=MovieForm
    template_name="movie_form.html"
    success_url="/success/"

class MovieDeleteView(LoginRequiredMixin,DeleteView):
    model=MovieInfo
    template_name="Confirm_delete.html"
    success_url=reverse_lazy('movie_form_create')

class MovieFormView(LoginRequiredMixin,ListView):
    model=MovieInfo
    template_name='formlist.html'
    context_object_name="movie"

def success(request):
    return render(request,"Confirm_success.html")



def view_headers(request):
    # user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
    # authorization = request.META.get('HTTP_AUTHORIZATION', 'No authorization header')
    # language=request.META.get('HTTP_ACCEPT_LANGUAGE')

    resp=[]
    for key,value in request.META.items():
        resp.append(f"{key}: {value}<br/>")
    return(HttpResponse(resp))
    
    # Return a response with header details
    return HttpResponse(f'User-Agent: {user_agent},<br/> Authorization: {authorization},<br/> Language: {language}')


def view_custom_header(request):
    response = HttpResponse("<h1>Hello, world!<h1/>")
    response['X-Custom-Header'] = 'Custom header value by Sree'
    return response




def query_string(request):
    # Get a parameter 'name' from the query string (e.g., ?name=John)
    name = request.GET.get('name', 'Guest')  # Default to 'Guest' if 'name' is not in query string
    return HttpResponse(f'Hello, {name}!')




