from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUserModel(AbstractUser):
    USER=[
        ('recruiter', 'Recruiter'),
        ('jobseeker', 'JobSeeker'),
    ]
    BLOOD_GROOP=[
        ('A+', 'A positive'),
        ('A-', 'A negative'),
        ('B+', 'B positive'),
        ('B-', 'B negative'),
        ('AB+', 'AB positive'),
        ('AB-', 'AB negative'),
        ('O+', 'O positive'),
        ('O-', 'O negative'),
    ]
    Fname=models.CharField(max_length=100, null=True)
    Lname=models.CharField(max_length=100, null=True)
    ProfilePicture=models.ImageField(upload_to='media/ProfilePic', null=True)
    DateOfBirth=models.DateField(auto_now_add=True, null=True)
    Address=models.CharField(max_length=100, null=True)
    BloodGroup=models.CharField(choices=BLOOD_GROOP ,max_length=100, null=True)
    UserType=models.CharField( choices=USER, max_length=100, null=True)

    # def __str__(self):
    #     return self.username
    
class AddJobModel(models.Model):
    JobTitle=models.CharField(max_length=100, null=True)
    CompanyName=models.CharField(max_length=100, null=True)
    Address=models.CharField(max_length=100, null=True)
    CompanyDescription=models.CharField(max_length=100, null=True)
    JobDescription=models.CharField(max_length=100, null=True)
    Qualification=models.CharField(max_length=100, null=True)
    SalaryInformation=models.CharField(max_length=100, null=True)
    Deadline=models.CharField(max_length=100, null=True)
    Designation=models.CharField(max_length=100, null=True)
    Experience=models.CharField(max_length=100, null=True)
    OwnerOfJobPost=models.CharField(max_length=100, null=True)
    Created_by=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.JobTitle