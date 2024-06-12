from django.contrib import admin
from .models import *

# Register your models here.

class CustomUserModelDisplay(admin.ModelAdmin):
    list_display=['username','email','user_type','city']
    search_fields=['username','email','user_type','city']
    
    fieldsets=[
        (
            "This is my title",
            {
            'fields':['username','email','password']
            }
        ),
        (
            "Advanced options",
            {
                'classes':['collapse'],
                'fields':['first_name','last_name','city','profile_pic','user_type']
            }
        )
    ]

admin.site.register(CustomUserModel,CustomUserModelDisplay)
admin.site.register(CategoryModel)
admin.site.register(TaskModel)
