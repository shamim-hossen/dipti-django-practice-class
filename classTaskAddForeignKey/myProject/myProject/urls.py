from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myProject.views import signUp,signIn, dashboard, addJob, viewJob, profile, logOutPage, viewListJob, delListJob, editJob, updateJob

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signIn, name='signIn'),
    path('signUp/', signUp, name='signUp'),
    path('dashboard/', dashboard, name='dashboard'),
    path('addJob/', addJob, name='addJob'),
    path('delListJob/<str:myid>', delListJob, name='delListJob'),
    path('editJob/<str:myid>', editJob, name='editJob'),
    path('updateJob/', updateJob, name='updateJob'),
    path('viewJob/<str:myid>/', viewJob, name='viewJob'),
    path('profile/', profile, name='profile'),
    path('logOutPage/', logOutPage, name='logOutPage'),
    path('viewListJob/', viewListJob, name='viewListJob'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
