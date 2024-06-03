from django.contrib import admin
from job_app.models import CustomUser, AddJobModel,RecruiterModel,SeekerModel
# Register your models here.
class CustomUserDisplay(admin.ModelAdmin):
    list_display = ['username','role','gender','city']
admin.site.register(CustomUser,CustomUserDisplay)
admin.site.register(AddJobModel)
admin.site.register(SeekerModel)
admin.site.register(RecruiterModel)
