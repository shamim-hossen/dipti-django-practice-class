from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUserModel(AbstractUser):
    GENDER=[
        ('male','Male'),
        ('female','Female'),
    ]
    Gender=models.CharField(choices=GENDER,max_length=100, null=True)
    Age=models.CharField(max_length=100, null=True)
    City=models.CharField(max_length=100, null=True)
    Country=models.CharField(max_length=100, null=True)
    USER_TYPE=[
        ('chef','Chef'),
        ('viewer','Viewer'),
    ]
    UserType=models.CharField(choices=USER_TYPE,max_length=100, null=True)

    def __str__(self):
        return self.username
    
class RecipeModel(models.Model):
    Title=models.CharField(max_length=100, null=True)
    RecipeImage=models.ImageField(upload_to='static/recipeimg', null=True)
    Description=models.CharField(max_length=100, null=True)
    PrepTime=models.CharField(max_length=100, null=True)
    CookTime=models.CharField(max_length=100, null=True)
    Servings=models.CharField(max_length=100, null=True)
    OwnerOfPost=models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Title