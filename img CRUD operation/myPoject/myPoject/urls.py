from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myPoject.views import student, addstudent,delstudent,editstudent, updatestudent, viewstudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', student, name='student'),
    path('addstudent/', addstudent, name='addstudent'),
    path('delstudent/<str:myid>', delstudent, name='delstudent'),
    path('editstudent/<str:myid>', editstudent, name='editstudent'),
    path('viewstudent/<str:myid>', viewstudent, name='viewstudent'),
    path('updatestudent/', updatestudent, name='updatestudent'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
