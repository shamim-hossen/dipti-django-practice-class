from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Shamim_06_JobPortal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('home/', home, name='home'),
    path('signout/', signout, name='signout'),
    path('profile/', profile, name='profile'),
    path('addjob/', addjob, name='addjob'),
    path('joblist/', joblist, name='joblist'),
    path('deletejob/<str:jobid>', deletejob, name='deletejob'),
    path('editjob/<str:jobid>', editjob, name='editjob'),
    path('applyjob/<str:jobid>', applyjob, name='applyjob'),
    path('skillset/', skillset, name='skillset'),
    path('companyinfo/', companyinfo, name='companyinfo'),
    path('basicinfo/', basicinfo, name='basicinfo'),
    path('postedjob/', postedjob, name='postedjob'),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
