from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import crudapp.views
import crudmember.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crudapp.views.home, name='home'),
    path('crudapp/', include('crudapp.urls')),
    path('crudmember/', include('crudmember.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
