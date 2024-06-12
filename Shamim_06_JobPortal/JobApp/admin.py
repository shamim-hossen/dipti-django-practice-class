from django.contrib import admin
from JobApp.models import *
# Register your models here.
class CustomUserDisplay(admin.ModelAdmin):
    list_display=['username','email','user_type']
admin.site.register(CustomUserModel,CustomUserDisplay)
admin.site.register(RecruiterModel)
admin.site.register(SeekerModel)
admin.site.register(JobModel)
admin.site.register(JobApplyModel)