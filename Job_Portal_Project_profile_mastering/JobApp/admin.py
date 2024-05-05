from django.contrib import admin
from JobApp.models import CustomUserModel, AddJobModel, RecruiterProfileModel,RecruiterContactInfo, SeekerProfileModel,SeekerBasicInfoModel,SeekerEducationQualificationModel,SeekerWorkExperienceModel,SeekerContentModel
# Register your models here.
class CustomUserDisplay(admin.ModelAdmin):
    list_display=['username','UserType','Age','BloodGroup','City','Country']
admin.site.register(CustomUserModel, CustomUserDisplay)
admin.site.register(AddJobModel)
admin.site.register(RecruiterProfileModel)
admin.site.register(SeekerProfileModel)
admin.site.register(RecruiterContactInfo)
admin.site.register(SeekerBasicInfoModel)
admin.site.register(SeekerEducationQualificationModel)
admin.site.register(SeekerWorkExperienceModel)
admin.site.register(SeekerContentModel)