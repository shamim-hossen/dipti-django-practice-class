from django.contrib import admin
from django.urls import path
from Shamim_06_JobPortal.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    # user authentication
    path('', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
    # Dashboard
    path('home/', home, name='home'),
    
    # job
    path('addjob/', addjob, name='addjob'),
    path('joblist/', joblist, name='joblist'),
    path('deletejob/<str:jobid>', deletejob, name='deletejob'),
    path('editjob/<str:jobid>', editjob, name='editjob'),
    path('viewjob/<str:jobid>', viewjob, name='viewjob'),
    path('applyjob/<str:jobid>', applyjob, name='applyjob'),
    path('jobsearch/',jobsearch,name='jobsearch'),
    path('appliedjob/',appliedjob,name='appliedjob'),
    
    # profile
    path('profile/',profile,name='profile'),
    path('basicinfo/',basicinfo,name='basicinfo'),
    path('seekerinfo/',seekerinfo,name='seekerinfo'),
    path('recruiterinfo/',recruiterinfo,name='recruiterinfo'),
    path('changepassword/',changepassword,name='changepassword'),
    path('editbasicinfo/',editbasicinfo,name='editbasicinfo'),
    path('editseekerprofile/',editseekerprofile,name='editseekerprofile'),
    path('editrecruiterprofile/',editrecruiterprofile,name='editrecruiterprofile'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
