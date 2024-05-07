from django.contrib import admin
from .models import*
# Register your models here.

class custom_user_display(admin.ModelAdmin):
    list_display = ['username','user_type','email']

class addjobModel_display(admin.ModelAdmin):
    list_display = ['job_title','job_type','salary']

admin.site.register(custom_user,custom_user_display)
admin.site.register(addjobModel,addjobModel_display)
admin.site.register(job_recruiter_profile)
admin.site.register(job_seeker_profile)
admin.site.register(basic_info)
admin.site.register(education)
admin.site.register(contact)
admin.site.register(experience)
