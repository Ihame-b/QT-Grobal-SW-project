from django.shortcuts import render
from rest_framework import generics,views, permissions
from .models import *
from django.views.generic.detail import DetailView
from rest_framework.response import Response
from TaskAPI.models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
#UIs


class Tasklist1(ListView):
    model = Task
    context_object_name ='tasks'
    template_name = 'task_list.html'

class TaskDetails1(DetailView):
    model =Task
    context_object_name = 'task'
    template_name = 'base/task.html'
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
