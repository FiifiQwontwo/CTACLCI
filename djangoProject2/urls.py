from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import ctac.urls

urlpatterns = [
    path('me/', admin.site.urls),
    path('', include('ctac.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
