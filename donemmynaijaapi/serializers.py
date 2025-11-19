from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from .utils import send_email

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
    
    def validate(self, data):
         if data['password1'] != data['password2']:
            return serializers.ValidationError("Passwords do not match.")
         
        #  if data['email'].exists():
        #    return serializers.ValidationError("Email already in use.")

        # if data['username'].exists():
        #    return serializers.ValidationError("Username already in use.")

        # if data['username'] in User.objects.all():
        #    return serializers.ValidationError("Username already in use.")
    

    def create(self, validated_data):
            username=validated_data.pop('username'),
            email=validated_data.pop('email'),
            password=validated_data.pop('password1'),

            # pop is to remove and add to variables

            user = User.objects.create_user(username=username, email=email, password=password)
            profile = Profile.objects.create(
               user=user,
               fullname=validated_data['fullname'],
               # validated is to get data from the serializer
               gender=validated_data['gender'],
               phone=validated_data['phone'],
               photo=validated_data['photo']                                
                                             
          )
            
            # send email to the registered email
            send_email(username, email)
            return profile