from django.contrib import admin
from myApp.models import CustomUserModel, RecipeModel, RecruiterProfileModel
# Register your models here.
class CustomUserDisplay(admin.ModelAdmin):
    list_display=['username','Gender','Age','City','Country','UserType',]
admin.site.register(CustomUserModel,CustomUserDisplay)
admin.site.register(RecipeModel)
admin.site.register(RecruiterProfileModel)
