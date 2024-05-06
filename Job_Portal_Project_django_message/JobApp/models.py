from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUserModel(AbstractUser):
    GENDER=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
    USER_TYPE=[
        ('jobseeker','Job Seeker'),
        ('jobrecruiter','Job Recruiter'),
    ]

    Age=models.CharField(max_length=100, null=True)
    Gender=models.CharField(choices=GENDER,max_length=100, null=True)
    BloodGroup=models.CharField(max_length=100, null=True)
    UserType=models.CharField(choices=USER_TYPE,max_length=100, null=True)
    City=models.CharField(max_length=100, null=True)
    Country=models.CharField(max_length=100, null=True)
    Profile_photo=models.ImageField(upload_to='static/propic', null=True)
    def __str__(self):
        return self.username

class AddJobModel(models.Model):
    Job_Type=[
        ('full_time','FullTime'),
        ('part_time','PartTime'),
    ]
    Work_place=[
        ('remote','Remote'),
        ('on_site','OnSite'),
    ]
    JobTitle=models.CharField(max_length=100, null=True)
    JobDescription=models.TextField( null=True)
    JobLocation=models.CharField(max_length=100, null=True)
    Deadline=models.CharField(max_length=100, null=True)
    CompanyLogo=models.ImageField(upload_to='static/jobpic', null=True)
    Requirements=models.TextField( null=True)
    Qualification=models.CharField(max_length=100, null=True)
    JobType=models.CharField(choices=Job_Type, max_length=100, null=True)
    Workplace=models.CharField(choices=Work_place,max_length=100, null=True)
    Salary=models.CharField(max_length=100, null=True)
    Experience=models.CharField(max_length=100, null=True)
    Created_By=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.Created_By.username

class RecruiterProfileModel(models.Model):
    user=models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='recruiterprofilemodel')
    CompanyName=models.CharField(max_length=100)
    CompanyLocation=models.CharField(max_length=100)
    RecruiterName=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
    
class RecruiterContactInfo(models.Model):
    user=models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='recruitercontactinfo')
    Phone=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
    
class SeekerLastEducation(models.Model):
    DEGREE=[
        ('jsc','JSC'),
        ('ssc','SSC'),
        ('hsc/diploma','HSC/DIPLOMA'),
        ('bsc','BSC'),
        ('msc','MSC'),
    ]

    user=models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='seekerlasteducation')
    degree = models.CharField(max_length=100,choices=DEGREE)
    institute = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    passing_year  = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class SeekerProfileModel(models.Model):
    user=models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='seekerprofilemodel')
    Qualification=models.CharField(max_length=100)
    Experience=models.CharField(max_length=100)
    Skills=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
    
class SeekerBasicInfoModel(models.Model):
    user=models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='Seekerbasicinfomodel')
    Qualification=models.CharField(max_length=100)
    Experience=models.CharField(max_length=100)
    Skill=models.CharField(max_length=100)
    Resume=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

class SeekerEducationQualificationModel(models.Model):
    user=models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='seekereducationqualificationmodel')
    EducationInstitution=models.CharField(max_length=100)
    EducationDegree=models.CharField(max_length=100)
    GraduationYear=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
    
class SeekerWorkExperienceModel(models.Model):
    user=models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='seekerworkexperiencemodel')
    WorkExperienceTitle=models.CharField(max_length=100)
    WorkExperienceCompany=models.CharField(max_length=100)
    WorkExperienceDescription=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
    

class SeekerContentModel(models.Model):
    user=models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='seekercontentmodel')
    SeekerDescription=models.TextField()
    CareerSummary=models.TextField()
    def __str__(self):
        return self.user.username





























