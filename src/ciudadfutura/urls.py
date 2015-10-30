from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('ciudadfutura.apps.cart.urls', namespace='cart')),
    url(r'^', include('ciudadfutura.apps.site.urls', namespace='site')),
    url(r'^', include('ciudadfutura.apps.mision.urls', namespace='mision')),
    url(r'^', include('ciudadfutura.apps.admin.urls', namespace='admin')),
]
