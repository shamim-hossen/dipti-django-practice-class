from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class DepartmentAddModel(models.Model):
    Department_Name=models.CharField(max_length=100)
    Head_of_Department=models.CharField(max_length=100)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.Department_Name

class SessionAddModel(models.Model):
    Session_Year=models.CharField(max_length=100)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.Session_Year

class CustomUserModel(AbstractUser):
    USER_TYPE={
        ('1','admin'),
        ('2','teacher'),
        ('3','student'),
    }
    user_type = models.CharField(choices=USER_TYPE,max_length=100)
    user_img = models.ImageField(upload_to='static/user_img')
    def __str__(self):
        return self.username
    
class StudentAddModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE)
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Student_Id=models.CharField(max_length=100)
    GENDER={
        ("male","Male"),
        ("female","Female"),
        ("others","Others"),
    }
    Gender=models.CharField(max_length=100,choices=GENDER)
    SECTION={
        ('1','A'),
        ('2','B'),
        ('3','C'),
        ('4','D'),
    }
    Section=models.CharField(choices=SECTION,max_length=100)
    Date_of_Birth=models.DateField()
    Department_Name=models.CharField(max_length=100)
    Religion=models.CharField(max_length=100)
    Mobile_Number=models.CharField(max_length=100)
    SESSION_OPTION={
        ('1',"Summer Session"),
        ('2',"Fall Session"),
        ('3',"Spring Session"),
    }
    Session_Year=models.CharField(choices=SESSION_OPTION,max_length=100)
    Student_Image=models.ImageField(upload_to='static/Student_Image')
    Father_Name=models.CharField(max_length=100)
    Father_Occupation=models.CharField(max_length=100)
    Father_Mobile=models.CharField(max_length=100)
    Father_Email=models.EmailField(max_length=100)
    Mother_Name=models.CharField(max_length=100)
    Mother_Occupation=models.CharField(max_length=100)
    Mother_Mobile=models.CharField(max_length=100)
    Mother_Email=models.EmailField(max_length=100)
    Present_Address=models.TextField()
    Permanent_Address=models.TextField()
    
    myDepartment=models.ForeignKey(DepartmentAddModel,on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.First_Name
    