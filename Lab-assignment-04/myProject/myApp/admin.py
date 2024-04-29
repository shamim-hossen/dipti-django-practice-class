from django.contrib import admin
from myApp.models import CustomUserModel, RecipeModel
# Register your models here.
class CustomUserDisplay(admin.ModelAdmin):
    list_display=['username','email','Gender','Age','UserType','City','Country']
admin.site.register(CustomUserModel, CustomUserDisplay)
admin.site.register(RecipeModel)
