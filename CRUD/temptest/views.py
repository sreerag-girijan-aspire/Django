from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from movies.models import MovieInfo
from temptest.api.serializers import MovieSerializer,RegisterSerializer,LoginSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets



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
@permission_classes([IsAuthenticated])
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

class RegisterAPI(APIView):
    def post(self,request):
        data=request.data
        serializer=RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({"message":serializer.errors},status=status.HTTP_404_NOT_FOUND)
        
        serializer.save()

        return Response({"message":"User Created"},status=status.HTTP_201_CREATED)
    

class LoginAPI(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def post(self,request):
        data=request.data
        serializer=LoginSerializer(data=data)

        if not serializer.is_valid():
            return Response({"message":serializer.errors},status=status.HTTP_404_NOT_FOUND)
        user=authenticate(username=serializer.data["username"],password=serializer.data["password"])

        if not user:
            return Response({"message":"Invalid"},status=status.HTTP_404_NOT_FOUND)
        
        token,_=Token.objects.get_or_create(user=user)

        return Response({"message":"Login Successful","token":str(token)},status=status.HTTP_200_OK)
    

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class=MovieSerializer
    queryset=MovieInfo.objects.all()


    def list(self, request):
        search=request.GET.get("search")
        queryset=self.queryset
        if search:
            queryset=queryset.filter(title__startswith=search.upper())
        serializer=MovieSerializer(queryset,many=True)
        return Response({"status":200,"data":serializer.data})