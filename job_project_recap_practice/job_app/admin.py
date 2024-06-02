from django.contrib import admin
from job_app.models import CustomUser, AddJobModel
# Register your models here.]
class CustomUserDisplay(admin.ModelAdmin):
    list_display = ['username','gender','user_type']
admin.site.register(CustomUser, CustomUserDisplay)
admin.site.register(AddJobModel)
