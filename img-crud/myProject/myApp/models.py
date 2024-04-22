from django.db import models

# Create your models here.
class StudentModel(models.Model):
    Name=models.CharField(max_length=100, null=True)
    Roll=models.CharField(max_length=100, null=True)
    Dept=models.CharField(max_length=100, null=True)
    Img=models.ImageField(upload_to='media/StudentImage', null=True)

    def __str__(self):
        return self.Name
