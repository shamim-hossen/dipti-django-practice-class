from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myProject.views import studentPage, addStudent, deleteStudent, editStudent, updateStudent, viewStudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', studentPage, name='studentPage'),
    path('addStudent/', addStudent, name='addStudent'),
    path('deleteStudent/<str:myid>', deleteStudent, name='deleteStudent'),
    path('editStudent/<str:myid>', editStudent, name='editStudent'),
    path('updateStudent/', updateStudent, name='updateStudent'),
    path('viewStudent/<str:myid>', viewStudent, name='viewStudent'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
