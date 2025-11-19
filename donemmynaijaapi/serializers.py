from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileSerializer(serializers.Serializer):
        class Meta:
            model = UserSerializer()
            fields = ['fullname', 'username', 'email', 'gender', 'phone', 'photo']

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Profile()
        fields = ['user', 'fullname', 'username', 'email', 'gender', 'phone', 'photo']