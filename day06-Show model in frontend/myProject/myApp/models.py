from django.db import models

# Create your models here.
class StudentModel(models.Model):
    Name=models.CharField(max_length=100)
    Roll=models.CharField(max_length=100)
    Dept=models.CharField(max_length=100)

    def __str__(self):
        return self.Name+''+self.Roll