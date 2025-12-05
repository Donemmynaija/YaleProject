from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER = (
    ('Male','Male'),
    ('Female','Female'),
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    gender = models.CharField(max_length=6, choices=GENDER)
    phone = models.CharField(max_length=12)
    photo = models.ImageField( upload_to="profile",default="https://randomuser.me/api/portraits/men/83.jpg" , null=True, blank=True)
    
    def __str__(self):
        return self.fullname