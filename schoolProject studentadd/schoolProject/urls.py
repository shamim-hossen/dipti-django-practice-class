from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from schoolProject.views import *
from schoolProject.studentviews import *
from schoolProject.teacherviews import *
from schoolProject.departmentviews import *
from schoolProject.subjectviews import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #_______________Login-Register-Pages_______________#
    path('signuppage/',signuppage,name='signuppage'),
    path('',signinpage,name='signinpage'),
    path('logoutpage',logoutpage,name='logoutpage'),
    
    #_______________Profile-Pages_______________#
    path('profile',profile,name='profile'),
    
    #_______________Admin-Pages_______________#
    path('adminpage/',adminpage,name='adminpage'),
    
    #_______________Teacher-Pages_______________#
    path('teacherdashboard/',teacherdashboard,name='teacherdashboard'),
    path('teacherlist/',teacherlist,name='teacherlist'),
    path('teacheradd/',teacheradd,name='teacheradd'),
    path('teacherdetails/',teacherdetails,name='teacherdetails'),
    path('teacheredit/',teacheredit,name='teacheredit'),
    path('teacherdelete/',teacherdelete,name='teacherdelete'),

    #_______________Student-Pages_______________#
    path('studentdashboard/',studentdashboard,name='studentdashboard'),
    path('studentlist/',studentlist,name='studentlist'),
    path('studentadd/',studentadd,name='studentadd'),
    path('studentdetails/<str:stuid>',studentdetails,name='studentdetails'),
    path('studentedit/<str:stuid>',studentedit,name='studentedit'),
    path('studentadelete/<str:stuid>',studentadelete,name='studentadelete'),
    
    #_______________Department-Pages_______________#
    path('departmentslist/',departmentslist,name='departmentslist'),
    path('departmentsadd/',departmentsadd,name='departmentsadd'),
    path('departmentsedit/',departmentsedit,name='departmentsedit'),
    path('departmentsdelete/',departmentsdelete,name='departmentsdelete'),
    
    #_______________Subject-Pages_______________#
    path('subjectslist/',subjectslist,name='subjectslist'),
    path('subjectsadd/',subjectsadd,name='subjectsadd'),
    path('subjectsedit/',subjectsedit,name='subjectsedit'),
    path('subjectsdelete/',subjectsdelete,name='subjectsdelete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)