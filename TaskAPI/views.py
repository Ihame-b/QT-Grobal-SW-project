from django.shortcuts import render
from rest_framework import generics,views, permissions
from .serializers import *
from .models import *
from django.views.generic.detail import DetailView
from rest_framework.response import Response
import requests
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# def get_weather_data(Task):
#        api_url = f"http://127.0.0.1:8000/api/"
#        response = requests.get(api_url)
#        data = response.json()
#        return data

# def weather_view(request, Task):
#        weather_data = get_weather_data(Task)
#        context = {'weather_data': weather_data}
#        return render(request, 'weather_template.html', context)

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

class Tasklist1(ListView):
    model = Task
    context_object_name ='tasks'
   

class TaskDetails1(DetailView):
    model =Task
    context_object_name = 'task'
    template_name = 'TaskAPI/base/task.html'
    # success_url = reverse_lazy('tasks')

class TaskCreate1(CreateView):
    model= Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate1(UpdateView):
    model= Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete1(DeleteView):
    model= Task
    context_object_name ='task'
    success_url = reverse_lazy('tasks')
