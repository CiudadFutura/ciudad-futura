from django.conf.urls import include, url

from .views import *

urlpatterns = [

    url(r'^mision/$', IndexView.as_view(), name='index'),

    url(r'^mision/register/$', register, name='register'),


    # Admin urls (TODO: move to a separated app)
    url(r'^admin/$',
        admin_dashboard,
        name='admin-dashboard'),
    url(r'^admin/login/$',
        admin_login,
        name='admin-login'),
    url(r'^admin/logout/$',
        admin_logout,
        name='admin-logout'),

    # Tags urls
    url(r'^admin/tag/$',
        admin_tag_list,
        name='admin-tag-list'),
    url(r'^admin/tag/create/$',
        admin_tag_form,
        name='admin-tag-create'),
    url(r'^admin/tag/(?P<tag_id>\d+)/edit/$',
        admin_tag_form,
        name='admin-tag-edit'),
    url(r'^admin/tag/(?P<tag_id>\d+)/delete/$',
        admin_tag_delete,
        name='admin-tag-delete'),

    # User urls
    url(r'^admin/user/$',
        admin_user_list,
        name='admin-user-list'),
    url(r'^admin/user/create/$',
        admin_user_form,
        name='admin-user-create'),
    url(r'^admin/user/(?P<user_id>\d+)/$',
        admin_user_details,
        name='admin-user-details'),
    url(r'^admin/user/(?P<user_id>\d+)/edit/$',
        admin_user_form,
        name='admin-user-edit'),
    url(r'^admin/user/(?P<user_id>\d+)/delete/$',
        admin_user_delete,
        name='admin-user-delete'),
]
