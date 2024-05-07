from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class custom_user(AbstractUser):
    user_type=[('jobseeker','Jobseeker'),('recruiter','Recruiter')]
    gender = [('male','Male'),('female','Female')]
    blood_group = [('A+','A+'),('A-','A-'),('B+','B+')]

    user_type = models.CharField(choices=user_type,max_length=10)
    gender = models.CharField(choices=gender,max_length=10)
    blood_group = models.CharField(choices=blood_group,max_length=10)
    age=models.IntegerField(null=True)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='media/user')

class addjobModel(models.Model):
    job_type=[('fulltime','Full Time'),('parttime','Part Time')]
    work_place=[('onsite','Onsite'),('remote','Remote')]

    job_title=models.CharField(max_length=100)
    job_description=models.TextField()
    job_location=models.TextField()
    deadline=models.CharField(max_length=100)
    requirments=models.TextField()
    company_logo=models.ImageField(upload_to='media/company')
    qualification=models.CharField(max_length=100)
    job_type=models.CharField(choices=job_type,max_length=10)
    work_place=models.CharField(choices=work_place,max_length=10)
    salary=models.IntegerField()
    experience=models.CharField(max_length=100)
    create_by=models.ForeignKey(custom_user,on_delete=models.CASCADE,null=True)

class job_recruiter_profile(models.Model):
    company_name=models.CharField(max_length=100)
    company_location=models.TextField()
    user = models.OneToOneField(custom_user,on_delete=models.CASCADE,related_name='recruiter_profile')
    def __str__(self):
        return self.user.username

class job_seeker_profile(models.Model):
    qualification=models.CharField(max_length=100)
    experience=models.TextField()
    skills=models.TextField()
    user = models.OneToOneField(custom_user,on_delete=models.CASCADE,related_name='seeker_profile')
    def __str__(self):
        return self.user.username 
    
class basic_info(models.Model):
    user = models.OneToOneField(custom_user,on_delete=models.CASCADE,related_name='basic_info')
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    
    
class education(models.Model):
    user = models.OneToOneField(custom_user,on_delete=models.CASCADE,related_name='education')
    degree = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    passing_year = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username +' - '+ self.degree
    
class experience(models.Model):
    user = models.OneToOneField(custom_user,on_delete=models.CASCADE,related_name='experience')
    company_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    joining_date = models.CharField(max_length=100)
    leaving_date = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username +' - '+ self.company_name
    
class contact(models.Model):
    user = models.OneToOneField(custom_user,on_delete=models.CASCADE,related_name='contact')
    phone = models.CharField(max_length=100)
    phone = models.TextField()
    def __str__(self):
        return self.user.username +' - '+ self.phone