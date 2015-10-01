from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    # Admin urls
    url(r'^superadmin/', include(admin.site.urls)),

    url(r'^', include('ciudadfutura.apps.site.urls', namespace='site')),
    url(r'^', include('ciudadfutura.apps.mision.urls', namespace='mision')),
    url(r'^', include('ciudadfutura.apps.admin.urls', namespace='adminpanel')),
]
