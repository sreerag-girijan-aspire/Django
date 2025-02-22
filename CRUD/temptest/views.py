from django.shortcuts import render

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
