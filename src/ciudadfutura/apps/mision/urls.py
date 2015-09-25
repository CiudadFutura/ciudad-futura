from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^mision/$', views.index, name='mision'),
    url(r'^mision/register/$', views.register, name='mision-register'),


    # Admin urls (TODO: move to a separated app)
    url(r'^admin/$',
        views.admin_dashboard,
        name='admin-dashboard'),
    url(r'^admin/login/$',
        views.admin_login,
        name='admin-login'),
    url(r'^admin/logout/$',
        views.admin_logout,
        name='admin-logout'),

    # Tags urls
    url(r'^admin/tag/$',
        views.admin_tag_list,
        name='admin-tag-list'),
    url(r'^admin/tag/create/$',
        views.admin_tag_form,
        name='admin-tag-create'),
    url(r'^admin/tag/(?P<tag_id>\d+)/edit/$',
        views.admin_tag_form,
        name='admin-tag-edit'),
    url(r'^admin/tag/(?P<tag_id>\d+)/delete/$',
        views.admin_tag_delete,
        name='admin-tag-delete'),

    # User urls
    url(r'^admin/user/$',
        views.admin_user_list,
        name='admin-user-list'),
    url(r'^admin/user/create/$',
        views.admin_user_form,
        name='admin-user-create'),
    url(r'^admin/user/(?P<user_id>\d+)/$',
        views.admin_user_details,
        name='admin-user-details'),
    url(r'^admin/user/(?P<user_id>\d+)/edit/$',
        views.admin_user_form,
        name='admin-user-edit'),
    url(r'^admin/user/(?P<user_id>\d+)/delete/$',
        views.admin_user_delete,
        name='admin-user-delete'),
]
