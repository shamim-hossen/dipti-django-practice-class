from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from JobApp.models import *


class CustomUserForm(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields=UserCreationForm.Meta.fields+('email','display_name','user_type')
        
class CustomUserAuthForm(AuthenticationForm):
    class Meta:
        model=CustomUserModel
        fields=['username','password']

class RecruiterForm(forms.ModelForm):
    class Meta:
        model=RecruiterModel
        fields=['company_name','company_description']

class SeekerForm(forms.ModelForm):
    class Meta:
        model=SeekerModel
        fields=['skill_sets','resume']
        
class JobForm(forms.ModelForm):
    class Meta:
        model=JobModel
        fields=['job_title','job_description','number_of_openings','category','skill_sets']
        
class JobApplyForm(forms.ModelForm):
    class Meta:
        model=JobApplyModel
        fields=['skills','status']