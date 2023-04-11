from functools import partial
from lib2to3.pgen2 import token
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status
from . models import Post, User, employees
from . serializers import employeesSerializer, PostSerializer, UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


class employeeList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employee = employees.objects.all()
        serializer = employeesSerializer(employee, many=True)
        return Response(serializer.data)
 

class PostApiView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        
        qs = Post.objects.all()
        serializer_qs = PostSerializer(qs,many=True) # Serializing single Objects
        return Response({"data":serializer_qs.data})
        

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
         serializer.save()

         return Response(serializer.data)
        return Response(serializer.errors)

class PostApiGetByID(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request,pk, *args, **kwargs):
        
        qs = Post.objects.filter(id=pk)
        # print(qs.title)
        serializer_qs = PostSerializer(qs,many=True)
        print(serializer_qs)
        return Response({"data":serializer_qs.data})

    def put(self, request,pk, *args, **kwargs):   
        qs = Post.objects.filter(pk=pk)
        # print("before    ",qs.title)
        qs.title = request.data['title']
        qs.description = request.data['description']
        qs.save()
        return Response({"data":request.data,"msg":"Data Updated","STATUS":200}) 
        

from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUser(APIView):

    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
            return Response({'status':403, 'errors':serializer.errors, 'message':"something went wrong"})
    
        serializer.save()

        user = User.objects.get(username = serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response(
            {'status': 200, 
            'payload':serializer.data,
            'refresh':str(refresh),
            'access':str(refresh.access_token), 'message': 'Your data is saved' 
            
            }
        )



def test_view(request):
    data = " "
    return JsonResponse(data)


@api_view()
def home(request):
    return Response({
        'status':200,
        'message': "Django rest framework api view"
    })


# class PostSerializerUpdateView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def put(self,request,pk):
#         # cus_id = request.data['id']
#         qs = Post.objects.get(id=pk)
#         serializer = PostSerializer(qs,data=request.data,partial=True)
#         if not serializer.is_valid():
#             return Response({'status':403, 'errors':serializer.errors, 'message':"something went wrong"})
#         else:
#             serializer.save()
#             return Response({'status':200, "msg":"data created"})
#     def delete(self,request,pk):
#         qs = Post.objects.get(id=pk)
#         if qs:
#             qs.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)