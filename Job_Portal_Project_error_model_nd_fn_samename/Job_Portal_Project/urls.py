"""
URL configuration for Job_Portal_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from JobApp.views import*
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signin, name='signin'),
    path('signin/',signin, name='signin'),
    path('signup/',signup, name='signup'),
    path('signout/',signout, name='signout'),
    path('deshboard/',deshboard, name='deshboard'),
    path('addjob/',addjob, name='addjob'),
    path('profile/',profile, name='profile'),
    path('profile/editprofile/',editprofile, name='editprofile'),
    path('profile/basic_info/',basic_info, name='basic_info'),
    path('profile/education/',education, name='education'),
    path('profile/contact/',contact, name='contact'),
    path('profile/experience/',experience, name='experience'),
    path('jobdelete/<int:id>',jobdelete, name='jobdelete'),
    path('viewjob/<int:id>',viewjob, name='viewjob'),
    path('editjob/<int:id>',editjob, name='editjob'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
