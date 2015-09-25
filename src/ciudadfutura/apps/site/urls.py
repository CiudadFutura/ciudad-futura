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
    url(r'^user/$',
        views.index,
        name='ciudadfutura-user-dashboard'),
    url(r'^user/profile/$',
        views.index,
        name='ciudadfutura-user-profile'),
]
