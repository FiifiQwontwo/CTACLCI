from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ctac.views import *
# from account.views import
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import handler404, handler500, handler403, handler400

# def trigger_error(request):
#     division_by_zero = 1 / 0


urlpatterns = [
    path('mews/', admin.site.urls),
    path('', include('ctac.urls')),
    # path('sentry-debug/', trigger_error),
    path('search/', include('search.urls')),
    path('contact/', include('contact.urls')),
    path('auth_api/', obtain_auth_token)

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# handler404 = 'ctac.views.error_404'
# handler500 = 'ctac.views.error_500'
# # handler403 = 'ctac.views.error_403'
# # handler400 = 'ctac.views.error_400'
