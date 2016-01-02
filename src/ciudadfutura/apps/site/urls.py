from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$',
        views.index,
        name='ciudadfutura-home'),

    # User urls
    url(r'^user/login/$',
        views.user_login,
        name='login'),
    url(r'^user/logout/$',
        views.user_logout,
        name='logout'),

    url(r'^user/$',
        views.user_dashboard,
        name='ciudadfutura-user-dashboard'),
    url(r'^user/profile/$',
        views.user_public_profile,
        name='ciudadfutura-user-public-profile'),
    url(r'^user/private-profile/$',
        views.user_private_profile,
        name='ciudadfutura-user-private-profile'),
    url(r'^user/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        views.user_reset_confirm,
        name='ciudadfutura-user-reset-confirm'),
    url(r'^user/reset/$',
        views.user_reset,
        name='ciudadfutura-user-reset'),
    url(r'^user/change_password/$',
        views.user_change_password,
        name='ciudadfutura-user-change-password'),
    url(r'^user/circle/$',
        views.user_circle,
        name='ciudadfutura-user-circle'),
]
