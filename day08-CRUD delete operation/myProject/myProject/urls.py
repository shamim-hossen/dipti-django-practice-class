from django.contrib import admin
from django.urls import path
from myProject.views import studentPage, addStudent, deleteStudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', studentPage, name='studentPage'),
    path('addStudent/', addStudent, name='addStudent'),
    path('deleteStudent/<str:myid>', deleteStudent, name='deleteStudent'),
]
