from django.urls import path
from .views import *

urlpatterns = [
    #UIs
    path('', Tasklist1.as_view(), name='tasks'),
    path('task-display/<int:pk>/', TaskDetails1.as_view(), name='tasks'),
    path('task-create/', TaskCreate1.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate1.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete1.as_view(), name='task-delete')

]

 
