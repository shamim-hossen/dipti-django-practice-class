from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUserModel(AbstractUser):
    USER_TYPE=[
        ('seeker','Job Seeker'),
        ('recruiter','Recruiter'),
    ]
    display_name=models.CharField(max_length=100, null=True)
    user_type=models.CharField(choices=USER_TYPE, max_length=100, null=True)

    def __str__(self):
        return self.username

