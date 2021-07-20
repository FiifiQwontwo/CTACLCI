from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from account.views import

# def trigger_error(request):
#     division_by_zero = 1 / 0


urlpatterns = [
    path('mews/', admin.site.urls),
    path('', include('ctac.urls')),
    path('account/', include('account.urls')),
    # path('sentry-debug/', trigger_error),
    path('', include('search.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# handler404 = 'ctac.views.error_404'
# handler500 = 'ctac.views.handler500'
# handler403 = 'ctac.views.error_403'
# handler400 = 'ctac.views.error_400'
