from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myProject.views import signin,signup,dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
