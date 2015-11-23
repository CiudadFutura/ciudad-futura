from django.conf.urls import include, url
from django.contrib.auth.forms import PasswordChangeForm

from . import views


urlpatterns = [
    url(r'^$',
        views.index,
        name='ciudadfutura-home'),

    # User urls
    url(r'^user/login/$',
        views.user_login,
        name='ciudadfutura-user-login'),
    url(r'^user/logout/$',
        views.user_logout,
        name='ciudadfutura-user-logout'),
    url(r'^user/$',
        views.user_dashboard,
        name='ciudadfutura-user-dashboard'),
    url(r'^user/profile/$',
        views.user_profile,
        name='ciudadfutura-user-profile'),
    url(r'^user/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        views.user_reset_confirm,
        name='ciudadfutura-user-reset-confirm'),
    url(r'^user/reset/$',
        views.user_reset,
        name='ciudadfutura-user-reset'),
    url(r'^user/change_password/$',
        views.user_change_password,
        name='ciudadfutura-user-change_password'),
]
