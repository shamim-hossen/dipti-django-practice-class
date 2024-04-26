from django.contrib import admin
from django.urls import path
from myProject.views import homepage, newspage, aboutpage, contactpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('newspage/', newspage, name='newspage'),
    path('aboutpage/', aboutpage, name='aboutpage'),
    path('contactpage/', contactpage, name='contactpage'),

]
