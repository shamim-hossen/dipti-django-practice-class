from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myProject.views import signup, signin, dashboard, logoutpage, profile, addrecipe, viewrecipe,deleterecipe, editrecipe, updaterecipe, viewfull

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logoutpage/', logoutpage, name='logoutpage'),
    path('profile/', profile, name='profile'),
    path('addrecipe/', addrecipe, name='addrecipe'),
    path('viewrecipe/', viewrecipe, name='viewrecipe'),
    path('deleterecipe/<str:myid>', deleterecipe, name='deleterecipe'),
    path('editrecipe/<str:myid>', editrecipe, name='editrecipe'),
    path('viewfull/<str:myid>', viewfull, name='viewfull'),
    path('updaterecipe/', updaterecipe, name='updaterecipe'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
