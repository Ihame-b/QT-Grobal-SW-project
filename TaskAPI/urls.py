from django.urls import path
from .views import *
from . import views
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView

urlpatterns = [

    #APIs
    path('', ListTask.as_view(), name='display'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('delete/<int:pk>', TaskDelete.as_view(), name='delete'),
    path('update/<int:pk>/', TaskUpdates.as_view(), name='update'),
    path('search/<int:pk>/', TaskSearch.as_view(), name='search'),
#     path('login/', UserLogIn.as_view(), name='login'),
#     path('profile/', ProofileView.as_view(), name='profile'),
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
   
      #UIs
    path('home/', Tasklist1.as_view(), name='tasks'),
    path('task-display/<int:pk>/', TaskDetails1.as_view(), name='tasks'),
    path('task-create/', TaskCreate1.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate1.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete1.as_view(), name='task-delete')

]