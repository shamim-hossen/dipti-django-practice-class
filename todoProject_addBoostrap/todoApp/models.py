from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    city=models.CharField(max_length=100,null=True)
    profile_pic=models.ImageField(upload_to='media/profile_pic',null=True)
    USER_TYPE={
        ('user','User'),
        ('admin','Admin'),
    }
    user_type=models.CharField(choices=USER_TYPE,max_length=100,null=True)
    
    class Meta:
        ordering=['username']
        verbose_name = 'Custom User Model'
        db_table='my_todo_list_table'
        unique_together = ["email", "username"]
        verbose_name_plural = "Custom User Models"
    
    def __str__(self):
        return self.username

class CategoryModel(models.Model):
    user=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True)
    category_name=models.CharField(max_length=100,null=True)
    created_at=models.DateField(auto_now_add=True,null=True)
    updated_at=models.DateField(auto_now=True,null=True)
    
    class Meta:
        ordering=['category_name']
        verbose_name = 'Category Model'
        db_table='todo_list_category_table'
        verbose_name_plural = "Category Models"
    
    def __str__(self):
        return self.category_name

class TaskModel(models.Model):
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    task_name=models.CharField(max_length=100,null=True)
    task_description=models.TextField(null=True)
    task_status=models.CharField(default='on_going',max_length=100,null=True)
    TASK_PRIORITY={
        ('high','High'),
        ('medium','Medium'),
        ('low','Low'),
    }
    task_priority=models.CharField(choices=TASK_PRIORITY,max_length=100,null=True)
    due_date=models.DateField(null=True)
    completed_date=models.DateField(null=True)
    created_at=models.DateField(auto_now_add=True,null=True)
    updated_at=models.DateField(auto_now=True,null=True)
    
    class Meta:
        ordering=['due_date']
        verbose_name = 'Task Model'
        db_table='todo_list_task_table'
        verbose_name_plural = "Task Models"
    
    # def __str__(self):
    #     return self.category