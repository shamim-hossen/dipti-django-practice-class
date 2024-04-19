from django.contrib import admin
from django.urls import path
from myProject.views import studentPage, home, news, about, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentPage/', studentPage, name='studentPage'),
    path('home/', home, name='home'),
    path('news/', news, name='news'),
    path('about/', about, name='about'),  
    path('contact/', contact, name='contact'),  
]
