from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^account/$',
        views.index,
        name='ciudadfutura-user-dashboard'),
    url(r'^account/profile/$',
        views.user_public_profile,
        name='ciudadfutura-user-public-profile'),
    url(r'^account/private-profile/$',
        views.user_private_profile,
        name='ciudadfutura-user-private-profile'),
    url(r'^account/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        views.user_reset_confirm,
        name='ciudadfutura-user-reset-confirm'),
    url(r'^account/reset/$',
        views.user_reset,
        name='ciudadfutura-user-reset'),
    url(r'^account/change_password/$',
        views.user_change_password,
        name='ciudadfutura-user-change-password'),
    url(r'^account/circle/$',
        views.user_circle,
        name='ciudadfutura-user-circle'),
]
