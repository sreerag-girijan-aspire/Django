from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def set_cookie(request):
    response = render(request, 'my_template.html')
    response.set_cookie('my_cookie', 'Custom_Cookie_Set_by_Sree', max_age=600)  # Set the cookie
    return response

def get_cookie(request):
    cookie_value = request.COOKIES.get('my_cookie', 'Default Value')
    return render(request, 'my_template.html', {'cookie_value': cookie_value})

def delete_cookie(request):
    response = render(request, 'my_template.html')
    response.delete_cookie('my_cookie')  # Delete the cookie
    return response




def set_session(request):
    request.session['user_name'] = 'Alice'
    return HttpResponse("Session data set to 'user_name: Alice'.")

def get_session(request):
    user_name = request.session.get('user_name', 'Guest')  # Default to 'Guest' if no session data
    return HttpResponse(f"Hello, {user_name}!")

def delete_session(request):
    try:
        del request.session['user_name']  # Delete the session data for 'user_name'
    except KeyError:
        pass
    return HttpResponse("Session data for 'user_name' deleted.")


def custom_tag(request):
    return render(request,"custom_tag_and_filter.html")

@api_view(["GET"])
def index():
    people_detal={
        "name":"Alex",
        "Age":"23"
    }
    return Response(people_detal)


