from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from todoApp.models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields=UserCreationForm.Meta.fields+('city','profile_pic','user_type','email','first_name','last_name')
        
class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model=CustomUserModel
        fields=['username','password']
        
class CustomCategoryForm(forms.ModelForm):
    class Meta:
        model=CategoryModel
        fields=['category_name']

class CustomTaskForm(forms.ModelForm):
    class Meta:
        model=TaskModel
        fields=['task_name','task_description','task_status','task_priority','due_date','completed_date']
        
        widgets={
            'due_date':forms.DateInput(attrs={'type':'date', 'class':'date-field'}),
            'completed_date':forms.DateInput(attrs={'type':'date','class':'date-field'}),
            'task_description':forms.Textarea(attrs={'type':'text','class':'textarea-field'})
        }
        
        labels={
            "task_description":"Enter description",
       }