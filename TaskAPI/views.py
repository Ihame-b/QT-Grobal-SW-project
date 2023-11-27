from django.shortcuts import render
from rest_framework import generics,views, permissions
from .serializers import *
from .models import *
from django.views.generic.detail import DetailView
from rest_framework.response import Response

# Create your views here.

class ListTask(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdates(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskSearch(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# class UserLogIn(views.APIView):
#     permission_classes = (permissions.AllowAny,)

# def post(self, request, format=None):
#     serializer = serializers.LoginSerializer(data=self.request.data,context={ 'request': self.request })
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data['user']
#     login(request, user)
#     return Response(None, status=status.HTTP_202_ACCEPTED)

# class ProofileView(generics.RetrieveAPIView):
#     serializer_class= serializers.BaseSerializer

#     def get_object(self):
#         return self.request.user