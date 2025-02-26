from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movies.models import MovieInfo
from temptest.api.serializers import MovieSerializer
from rest_framework.views import APIView


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


@api_view(["GET","POST","PATCH"])
def movie_view(request):
    if request.method=="GET":
        mov_obj=MovieInfo.objects.all()
        serializer=MovieSerializer(mov_obj,many=True)
        return Response((serializer.data))
    
    elif request.method=="POST":
        data=request.data
        serializer=MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method=="PATCH":
        data=request.data
        obj=MovieInfo.objects.get(id=data["id"])
        serializer=MovieSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



@api_view(["GET","DELETE"])
def delete(request,pk):
    if request.method=="GET":
        obj=MovieInfo.objects.get(pk=pk)
        serializer=MovieSerializer(obj)
        return Response((serializer.data))

    elif request.method=="DELETE":
        obj=MovieInfo.objects.get(pk=pk)
        obj.delete()
        return Response({"message":"Movie Deleted"})
    

class ApiViewMovies(APIView):
    def get(self,request):
        mov_obj=MovieInfo.objects.all()
        serializer=MovieSerializer(mov_obj,many=True)
        return Response(serializer.data)


    def post(self,request):
        data=request.data
        serializer=MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



