from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^', include('ciudadfutura.apps.site.urls', namespace='site')),
    url(r'^', include('ciudadfutura.apps.account.urls', namespace='account')),
    url(r'^', include('ciudadfutura.apps.mision.urls', namespace='mision')),
    url(r'^', include('ciudadfutura.apps.admin.urls', namespace='admin')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
