from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    GENDER = [
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]

    USERTYPE = [
        ('seeker','Seeker'),
        ('recruiter','Recruiter'),
    ]

    gender = models.CharField(max_length=100, choices=GENDER)
    user_type = models.CharField(max_length=100, choices=USERTYPE)
    profile_picture = models.ImageField(upload_to='static/propic')

    def __str__(self):
        return self.username
    
class AddJobModel(models.Model):
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    company_description = models.TextField()
    job_description = models.TextField()
    qualification = models.CharField(max_length=100)
    salary_information = models.CharField(max_length=100)
    deadline = models.DateField()
    designation = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    
    def __str__(self):
        return self.created_by.username