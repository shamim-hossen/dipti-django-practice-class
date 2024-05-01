from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myProject.views import signin, signup, dashboard, logoutfn, profile, viewrecipe, addrecipe, editrecipe, updaterecipe, deleterecipe, viewfullrecipe


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logoutfn/', logoutfn, name='logoutfn'),
    path('profile/', profile, name='profile'),
    path('viewrecipe/', viewrecipe, name='viewrecipe'),
    path('addrecipe/', addrecipe, name='addrecipe'),
    path('editrecipe/<str:myid>', editrecipe, name='editrecipe'),
    path('deleterecipe/<str:myid>', deleterecipe, name='deleterecipe'),
    path('viewfullrecipe/<str:myid>', viewfullrecipe, name='viewfullrecipe'),
    path('updaterecipe/', updaterecipe, name='updaterecipe'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
