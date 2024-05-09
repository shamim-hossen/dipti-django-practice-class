from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class job_portal_model(AbstractUser):
    gender=[
        ('male','Male'),
        ('female','Female'),
    ]
    blood=[
        ('A+','A+'),
        ('B+','B+'),
    ]
    user_type=[
        ('recruiter', 'Recruiter'), 
        ('seeker', 'Seeker'),
    ]
    gender=models.CharField(choices=gender,max_length=100)
    blood=models.CharField(choices=blood,max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/jobportal')
    user_type=models.CharField(choices=user_type,max_length=100)
    
class recruiter_model(models.Model):
    user=models.OneToOneField(job_portal_model,on_delete=models.CASCADE, related_name='recruiterprofile')
    company_name=models.CharField(max_length=100)
    company_location=models.CharField(max_length=100)
    recruiter_name=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.user.username
class seeker_model(models.Model):
    certificate=[
        ('ssc','ssc'),
        ('hsc','hsc'),
        ('diploma','diploma'),
    ]
    user=models.OneToOneField(job_portal_model,on_delete=models.CASCADE, related_name='seekerprofile')
    qualification=models.CharField(max_length=100, null=True)
    experience=models.CharField(max_length=100, null=True)
    skills=models.CharField(max_length=100, null=True)
    certificate=models.CharField(choices=certificate,max_length=100, null= True)
        
    def __str__(self) -> str:
        return self.user.username
    
class apply_job(models.Model):
    job_type=[
        ('Full_time','Full_time'),
        ('Part_time','Part_time'),
    ]
    
    workplace=[
        ('remote','remote'),
        ('On_site','On_site'),
    ]
    job_type=models.CharField(choices=job_type,max_length=100)
    workplace=models.CharField(choices=workplace,max_length=100)
    job_title=models.CharField(max_length=100)
    job_description=models.CharField(max_length=100)
    job_location=models.CharField(max_length=100)
    deadline=models.CharField(max_length=100)
    company_logo=models.ImageField(upload_to='media/applyjob')
    requirement=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)

class basic_information(models.Model):
    user=models.OneToOneField(job_portal_model,on_delete=models.CASCADE, related_name='basic_information')
    father_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    Parmanent_address=models.CharField(max_length=100)

class education(models.Model):
    user=models.OneToOneField(job_portal_model,on_delete=models.CASCADE, related_name='education')
    last_degree=models.CharField(max_length=100)
    passing_year=models.CharField(max_length=100)

class work_experience(models.Model):
    user=models.OneToOneField(job_portal_model,on_delete=models.CASCADE, related_name='work_experience')
    Possition=models.CharField(max_length=100)
    name_of_company=models.CharField(max_length=100)

class contact(models.Model):
    user=models.OneToOneField(job_portal_model,on_delete=models.CASCADE, related_name='contact')
    e_mail=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
