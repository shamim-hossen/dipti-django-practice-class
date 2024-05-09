from django.contrib import admin
from JobApp.models import *
# Register your models here.
class job_list(admin.ModelAdmin):
    list_display=('username', 'user_type')
    
admin.site.register(job_portal_model,job_list)
admin.site.register(recruiter_model)
admin.site.register(seeker_model)
admin.site.register(apply_job)
admin.site.register(basic_information)
admin.site.register(education)
admin.site.register(work_experience)
admin.site.register(contact)
