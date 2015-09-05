from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    # Admin urls
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('ciudadfutura.apps.site.urls')),
    url(r'^', include('ciudadfutura.apps.mision.urls')),
]
