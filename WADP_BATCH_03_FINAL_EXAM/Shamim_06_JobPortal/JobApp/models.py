from django.db import models
from django.contrib.auth.models import AbstractUser
    
# Create your models here.

class CustomUserModel(AbstractUser):
    display_name=models.CharField(max_length=100,null=True)
    USER_TYPE=[
        ('recruiter',"Job Recruiter"),
        ('seeker',"Job Seeker"),
    ]
    user_type=models.CharField(max_length=100,choices=USER_TYPE,null=True)

    def __str__(self):
        return self.username
    
class RecruiterModel(models.Model):
    recruiteruser=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='recruitermodel',null=True)
    company_name=models.CharField(max_length=100,null=True)
    company_address=models.TextField(null=True)

class SeekerModel(models.Model):
    seekeruser=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='seekermodel',null=True)
    Skills=models.CharField(max_length=100,null=True)
    Resume=models.FileField(upload_to='media/seekerResume',null=True)

class JobModel(models.Model):
    created_by=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True)
    Title=models.CharField(max_length=100)
    Number_openings=models.IntegerField(null=True)
    Category=models.CharField(max_length=100,null=True)
    Job_description=models.TextField(null=True)
    Skills=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.Title
    
class JobApplymodel(models.Model):
    applicant=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True)
    applied_job=models.ForeignKey(JobModel,on_delete=models.CASCADE,null=True)
    skills=models.CharField(max_length=100,null=True)
    resume=models.FileField(upload_to='media/applyResume',null=True)
    status=models.CharField(max_length=100,default="Pending",null=True)