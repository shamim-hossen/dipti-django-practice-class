from django.contrib import admin
from myApp.models import CustomUserModel
# Register your models here.
class CustomUserDisplay(admin.ModelAdmin):
    list_display=['username','UserType','BloodGroup','Address']
admin.site.register(CustomUserModel,CustomUserDisplay)
