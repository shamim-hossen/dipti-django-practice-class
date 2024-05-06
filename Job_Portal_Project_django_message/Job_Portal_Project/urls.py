from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Job_Portal_Project.views import signin, signup, dashboard,logoutfn, profile, addjob, viewalljob, editjob, deljob, updatejob, viewjob, appliedjob, postedjob, editprofile,profilebasicinfo, profilerecruitercontact, educationqualification, workexperience, content

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logoutfn/', logoutfn, name='logoutfn'),
    path('profile/', profile, name='profile'),
    path('addjob/', addjob, name='addjob'),
    path('editjob/<str:myid>', editjob, name='editjob'),
    path('deljob/<str:myid>', deljob, name='deljob'),
    path('viewjob/<str:myid>', viewjob, name='viewjob'),
    path('updatejob/', updatejob, name='updatejob'),
    path('viewalljob/', viewalljob, name='viewalljob'),
    path('appliedjob/', appliedjob, name='appliedjob'),
    path('postedjob/', postedjob, name='postedjob'),
    path('editprofile/', editprofile, name='editprofile'),
    path('profilebasicinfo/', profilebasicinfo, name='profilebasicinfo'),
    path('profilerecruitercontact/', profilerecruitercontact, name='profilerecruitercontact'),
    path('educationqualification/', educationqualification, name='educationqualification'),
    path('workexperience/', workexperience, name='workexperience'),
    path('content/', content, name='content'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
