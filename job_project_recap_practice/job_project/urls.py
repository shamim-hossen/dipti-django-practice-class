from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from job_project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signin,name='signin'),
    path('signup/',signup,name='signup'),
    path('signout/',signout,name='signout'),
    path('home/',home,name='home'),
    path('profile/',profile,name='profile'),
    path('cngpassword/',cngpassword,name='cngpassword'),
    path('cngpassword/',cngpassword,name='cngpassword'),
    path('basicinfo/',basicinfo,name='basicinfo'),
    path('addjob/',addjob,name='addjob'),
    path('viewalljob/',viewalljob,name='viewalljob'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
