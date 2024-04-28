from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUserModel(AbstractUser):
    USER=[
        ('seeker','JobSeeker'),
        ('recruiter','JobRecruiter'),
    ]
    BLOOD_GROUP=[
        ('AB+','AB positive'),
        ('AB-','AB Negative'),
        ('A+','A positive'),
        ('A-','A Negative'),
        ('B+','B positive'),
        ('B-','B Negative'),
        ('0+','O positive'),
        ('O-','O Negative'),
    ]
    ProfilePicture=models.ImageField(upload_to='media/Image')
    DateOfBirth=models.DateField(auto_now_add=True)
    Address=models.CharField(max_length=100)
    UserType=models.CharField(choices=USER, max_length=100)
    BloodGroup=models.CharField(choices=BLOOD_GROUP, max_length=100)