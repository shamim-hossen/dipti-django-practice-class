
from django.contrib import admin
from django.urls import path
from myProject.views import *
from myProject.myAdminviews import *
from myProject.teacherviews import *
from myProject.studentviews import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signinPage,name="signinPage"),
    path('signupPage/',signupPage,name="signupPage"),

    #-------Admin Route----------
    path('adminDashboard/',adminDashboard,name="adminDashboard"),

    #-------Admin student Route----------
    path('studentlist/',studentlist,name="studentlist"),
    path('studentadd/',studentadd,name="studentadd"),
    path('studentedit/',studentedit,name="studentedit"),

    #-------Admin teacher Route----------
    path('teacherlist/',teacherlist,name="teacherlist"),
    path('teacheradd/',teacheradd,name="teacheradd"),
    path('teacheredit/',teacheredit,name="teacheredit"),

    #-------Admin department Route----------
    path('departmentlist/',departmentlist,name="departmentlist"),
    path('departmentadd/',departmentadd,name="departmentadd"),
    path('departmentedit/',departmentedit,name="departmentedit"),

    #-------Admin subject Route----------
    path('subjectlist/',subjectlist,name="subjectlist"),
    path('subjectadd/',subjectadd,name="subjectadd"),
    path('subjectedit/',subjectedit,name="subjectedit"),


    #-------Teacher Route----------
    path('teacherDashboard/',teacherDashboard,name="teacherDashboard"),

    #-------Student Route----------
    path('studentdashboard/',studentdashboard,name="studentdashboard"),
]
