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

    # Person urls
    url(r'^admin/person/$',
        views.admin_person_list,
        name='admin-person-list'),
    url(r'^admin/person/create/$',
        views.admin_person_form,
        name='admin-person-create'),
    url(r'^admin/person/(?P<person_id>\d+)/$',
        views.admin_person_details,
        name='admin-person-details'),
    url(r'^admin/person/(?P<person_id>\d+)/edit/$',
        views.admin_person_form,
        name='admin-person-edit'),
    url(r'^admin/person/(?P<person_id>\d+)/delete/$',
        views.admin_person_delete,
        name='admin-person-delete'),
]
