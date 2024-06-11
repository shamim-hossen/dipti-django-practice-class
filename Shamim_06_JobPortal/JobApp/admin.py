from django.contrib import admin
from JobApp.models import *
# Register your models here.
class CustomUserDisplay(admin.ModelAdmin):
    list_display=['username','email','user_type']
admin.site.register(CustomUserModel,CustomUserDisplay)