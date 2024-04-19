from django.db import models

# Create your models here.
class PortfolioModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    categories=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class SkillModel(models.Model):
    name=models.CharField(max_length=100)
    categories=models.CharField(max_length=100)
    proficiency=models.CharField(max_length=100)

    def __str__(self):
        return self.name