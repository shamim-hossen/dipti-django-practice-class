from django.contrib import admin
from myApp.models import*
# Register your models here.

class CustomUserDisplayModel(admin.ModelAdmin):
    list_display=['Fname', 'username', 'Address', 'UserType','BloodGroup', 'DateOfBirth', 'ProfilePicture']
    
admin.site.register(CustomUserModel, CustomUserDisplayModel)
class AddJobDisplayModel(admin.ModelAdmin):
    list_display=['OwnerOfJobPost','JobTitle', 'CompanyName', 'Address', 'Qualification','SalaryInformation', 'Deadline', 'Designation','Experience']
admin.site.register(AddJobModel,AddJobDisplayModel)
