from django.contrib import admin
from django.urls import path
from myProject.views import studentPage, addStudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', studentPage, name='studentPage'),
    path('addStudent/', addStudent, name='addStudent'),

]
