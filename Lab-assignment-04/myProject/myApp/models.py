from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUserModel(AbstractUser):
    GENDER=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
    COUNTRY=[
        ('BD','Bangladesh'),
        ('IN','India'),
        ('PK','Pakistan'),
    ]
    USER_TYPE=[
        ('chef','Chef'),
        ('viewer','Viewer'),
    ]
    Gender=models.CharField(choices=GENDER, max_length=100, null=True)
    Age=models.CharField(max_length=100, null=True)
    City=models.CharField(max_length=100, null=True)
    Country=models.CharField(choices=COUNTRY, max_length=100, null=True)
    UserType=models.CharField(choices=USER_TYPE, max_length=100, null=True)


class RecipeModel(models.Model):
    TAG=[
        ('vegetarian','Vegetarian'),
        ('non-vegetarian','Non-vegetarian'),
    ]
    LEVEL=[
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),
    ]
    CATEGORIES=[
        ('breakfast','Breakfast'),
        ('lunch','Lunch'),
        ('dinner','Dinner'),
    ]

    RecipeTitle=models.CharField(max_length=100, null=True)
    Ingredients=models.CharField(max_length=100, null=True)
    Instructing=models.CharField(max_length=100, null=True)
    PreparationTime=models.CharField(max_length=100, null=True)
    CookingTime=models.CharField(max_length=100, null=True)
    TotalTime=models.CharField(max_length=100, null=True)
    DifficultyLevel=models.CharField(choices=LEVEL ,max_length=100, null=True)
    NutrationalInformation=models.CharField(max_length=100, null=True)
    SampleRecepeImage=models.ImageField(upload_to='media/Image', null=True)
    RecipeCategory=models.CharField(choices=CATEGORIES ,max_length=100, null=True)
    Tags=models.CharField(choices=TAG ,max_length=100, null=True)
    TotalCalories=models.CharField(max_length=100, null=True)
    OwnerOfJobPost=models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.RecipeTitle