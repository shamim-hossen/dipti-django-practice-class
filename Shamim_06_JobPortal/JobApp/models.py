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


class RecruiterModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,null=True,related_name='recruitermodel')
    company_name=models.CharField(max_length=100,null=True)
    company_description=models.TextField(null=True)
    
    def __str__(self):
        if self.user:
            return self.user.username
        else:
            return "No User"

class SeekerModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,null=True,related_name='seekermodel')
    skill_sets=models.CharField(max_length=100)
    resume=models.FileField(upload_to='static/resume',null=True)
    def __str__(self):
        if self.user:
            return self.user.username
        else:
            return "No User"
    
class JobModel(models.Model):
    created_by=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True,related_name='jobmodel')
    job_title=models.CharField(max_length=100,null=True)
    job_description=models.TextField(null=True)
    number_of_openings=models.IntegerField(null=True)
    category=models.CharField(max_length=100,null=True)
    skill_sets=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.job_title

class JobApplyModel(models.Model):
    user=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True)
    applied_job=models.ForeignKey(JobModel,on_delete=models.CASCADE,null=True)
    skills=models.CharField(max_length=100)
    status=models.CharField(default='Pending',max_length=100,null=True)
    
    def __str__(self):
        return self.user.username