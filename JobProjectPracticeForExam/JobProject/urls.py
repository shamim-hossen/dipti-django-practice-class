from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from JobProject.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signin, name='signin'),
    path('signup/',signup, name='signup'),
    path('signout/',signout, name='signout'),
    path('home/',home, name='home'),
    #recruiter 
    path('addjob/',addjob, name='addjob'),
    path('joblist/',joblist, name='joblist'),
    path('deletejob/<str:jobid>',deletejob, name='deletejob'),
    path('editjob/<str:jobid>',editjob, name='editjob'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
