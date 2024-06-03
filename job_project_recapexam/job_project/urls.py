from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from job_project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signin, name='signin'),
    path('signup/',signup, name='signup'),
    path('signout/',signout, name='signout'),
    path('home/',home, name='home'),
    path('profile/',profile, name='profile'),
    path('basicinfo/',basicinfo, name='basicinfo'),
    path('cngpass/',cngpass, name='cngpass'),
    path('addjob/',addjob, name='addjob'),
    path('viewalljob/',viewalljob, name='viewalljob'),
    path('deljob/<str:myid>',deljob, name='deljob'),
    path('editjob/<str:myid>',editjob, name='editjob'),
    path('updatejob/',updatejob, name='updatejob'),
    path('seekerinfo/',seekerinfo, name='seekerinfo'),
    path('recruiterinfo/',recruiterinfo, name='recruiterinfo'),
    path('education/',education, name='education'),
    path('experience/',experience, name='experience'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
