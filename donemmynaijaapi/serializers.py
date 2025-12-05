from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Profile
from . utils import send_email


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email"]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSerializer()
        fields = ["fullname","username","email","gender","phone","photo"]

class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Profile
        fields=  ["fullname","username","password1","password2","email","gender","phone","photo"]
    
    def validate(self,data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Password does not match")
        return data
    
    def create(self, validated_data):
        username= validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password1')

        user = User.objects.create_user(username=username,password=password, email=email)
        profile = Profile.objects.create(
            user = user,
            fullname = validated_data['fullname'],
            gender = validated_data['gender'],
            phone = validated_data['phone'],
            photo = validated_data['photo'],
        )
        # send email to the registered email
        send_email(username,email)
        return profile