from django.contrib import admin
from JobApp.models import *
# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(RecruiterModel)
admin.site.register(SeekerModel)
admin.site.register(JobModel)
admin.site.register(JobApplymodel)