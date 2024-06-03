from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    ROLE = [
        ('recruiter','Recruiter'),
        ('jobseeker','Job Seeker'),
    ]
    GENDER = [
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
    role = models.CharField(max_length=100, choices=ROLE, null=True)
    city = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, choices=GENDER, null=True)
    profile_picture = models.ImageField(upload_to='media/pic', null=True)

    def __str__(self):
        return self.username
    
class AddJobModel(models.Model):
    created_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    jobTitle = models.CharField(max_length=100)
    companyDescription = models.CharField(max_length=100)
    companyName = models.CharField(max_length=100)
    companyLocation = models.TextField()
    qualifications = models.TextField()
    deadline = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    
    def __str__(self):
        return self.created_by.username


class SeekerModel(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='seekermodel')
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    education_name=models.CharField(max_length=100)
    education_year=models.CharField(max_length=100)
    education_institute=models.CharField(max_length=100)
    education_qualification=models.CharField(max_length=100)
    work_experience = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
    
class RecruiterModel(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='recruitermodel')
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    Company_name=models.CharField(max_length=100)
    Company_location=models.CharField(max_length=100)
    Recruiter_Name=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

