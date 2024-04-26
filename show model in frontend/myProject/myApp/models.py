from django.db import models

# Create your models here.
class showModel(models.Model):
    Name=models.CharField(max_length=100)
    Roll=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Name