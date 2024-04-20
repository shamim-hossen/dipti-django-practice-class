from django.contrib import admin
from django.urls import path
from myProject.views import studentPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', studentPage, name='studentPage'),
]
