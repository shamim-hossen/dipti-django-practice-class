from django.contrib import admin
from schoolApp.models import *
# Register your models here.

class CustomUserModelDisplay(admin.ModelAdmin):
    list_display=['username','user_type']
    search_fields=['username','user_type']
    fieldsets=[
       ( 
            "User",
            {"fields":["username","email","user_type"],}
        ),
    ]

admin.site.register(CustomUserModel,CustomUserModelDisplay)
admin.site.register(StudentAddModel)
admin.site.register(DepartmentAddModel)
admin.site.register(SessionAddModel)

