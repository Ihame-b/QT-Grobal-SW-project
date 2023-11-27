from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'Assignee', 'title', 'description', 'priority', 'createTask', 'endTask', 'UploadFile', 'projects')

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(
#         label ="Username",
#         write_only = True
#     )
#     password = serializers.CharField(
#         label = "Password",
#         style ={'input_type': 'password'},
#         trim_whitespace = False,
#         write_only = True
#     )

# def validate(self, attrs):
#     username =attrs.get('username')
#     password = attrs.get('password')

#     if username and password:
#         user = authenticate(request=self.context.get('request'), username = username, password=password)
#         if not user:
#             msg = 'Access denied: wrong user and pass.' 
#             raise serializers.ValidationError(msg, code='authorization')
#     else:
#         msg = 'Both "username" and "password" are required.'
#         raise serializers.ValidationError(msg, code='authorization')
#     attrs['user'] =user 
#     return attrs

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =Task
#         fields =['usernasme', 'email', 'first_name', 'last_name']
