from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from todoProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # sign up / in , log out
    path('signup/',signup,name='signup'),
    path('',signin,name='signin'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logoutpage/',logoutpage,name='logoutpage'),
    
    # category
    path('addcategory/',addcategory,name='addcategory'),
    path('categorylist/',categorylist,name='categorylist'),
    path('categorydel/<str:catid>',categorydel,name='categorydel'),
    path('editcategory/<str:catid>',editcategory,name='editcategory'),
    
    # task 
    path('addtask/',addtask,name='addtask'),
    path('tasklist/',tasklist,name='tasklist'),
    path('taskdel/<str:taskid>',taskdel,name='taskdel'),
    path('edittask/<str:taskid>',edittask,name='edittask'),
    path('markascomp/<str:taskid>',markascomp,name='markascomp'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)