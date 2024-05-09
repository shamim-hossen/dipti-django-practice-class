from django.contrib import admin
from django.urls import path
from Job_Portal_Project.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', homepage, name='homepage'),
    path('', singin, name='singin'),
    path('singup/', singup, name='singup'),
    path('logoutpage/', logoutpage, name='logoutpage'),
    path('addjob/', addjob, name='addjob'),
    path('job_list/', job_list, name='job_list'),
    path('profile/', profile, name='profile'),
    path('editprofile/', editprofile, name='editprofile'),
    path('deletee/<str:myid>', deletee, name='deletee'),
    path('b_information/', b_information, name='b_information'),
    path('education_q/', education_q, name='education_q'),
    path('work_exp/', work_exp, name='work_exp'),
    path('con_tact/', con_tact, name='con_tact'),
    path('userprofile/', userprofile, name='userprofile'),
    path('change_passwordPage/', change_passwordPage, name='change_passwordPage'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
