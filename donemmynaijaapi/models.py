from django.db import models
from django.contrib.auth.models import User

# Create your models here:

# ( dis is to mix django default user model with custom profile model)
# class User(models.Model):
#    pass # Placeholder for user-related fields

# class Profile(models.Model):

#    def __str__(self):
#        pass # Placeholder for string representation

# Django relationship with User model

'''
1-to-1 relationship: One user has one profile
   (a student can have only one ID card)
   models.OneToOneField(User, on_delete=models.CASCADE)

One-to-many relationship: One user can have multiple posts
    (a blogger can write multiple blog posts)
    models.ForeignKey(User, on_delete=models.CASCADE)

Many-to-many relationship: Users can follow multiple users and be followed by multiple users
    (social media followers)
    models.ManyToManyField(User, related_name='followers', blank=True)
'''

# SHIRT_SIZE = (
#    ('S', 'Small'),
#    ('M', 'Medium'),
#    ('L', 'Large'),
#    ('XL', 'Extra Large'),
#)

GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
# gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    gender = models.CharField(max_length=10, choices=GENDER)
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to="profile_pictures/", default="https://randomuser.me/api/portraits/men/83.jpg", null=True, blank=True)
#    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.fullname