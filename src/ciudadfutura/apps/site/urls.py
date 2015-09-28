from django.conf.urls import include, url

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
]
