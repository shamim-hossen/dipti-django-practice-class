from django.db import models

# Create your models here.
class StudentModel(models.Model):
    ProfilePic=models.ImageField(upload_to='media/Image')
    Name=models.CharField(max_length=100)
    Roll=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    City=models.CharField(max_length=100)

    def __str__(self):
        return self.Name