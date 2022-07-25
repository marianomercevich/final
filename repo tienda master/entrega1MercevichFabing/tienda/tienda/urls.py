from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from tiendaapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tiendaapp/', include('tiendaapp.urls')),
    path('', entrada),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)