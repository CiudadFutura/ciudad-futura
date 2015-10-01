from django.conf.urls import url
from . import views

urlpatterns = [

    # Admin urls
    url(r'^admin/$', views.admin_dashboard, name='dashboard'),
    url(r'^admin/login/$', views.admin_login, name='login'),
    url(r'^admin/logout/$', views.admin_logout, name='logout'),

    # Tags urls
    url(r'^admin/tag/$', views.admin_tag_list, name='tag-list'),
    url(r'^admin/tag/create/$', views.admin_tag_form, name='tag-create'),
    url(r'^admin/tag/(?P<tag_id>\d+)/edit/$', views.admin_tag_form, name='tag-edit'),
    url(r'^admin/tag/(?P<tag_id>\d+)/delete/$', views.admin_tag_delete, name='tag-delete'),

    # User urls
    url(r'^admin/user/$', views.admin_user_list, name='user-list'),
    url(r'^admin/user/create/$', views.admin_user_form, name='user-create'),
    url(r'^admin/user/(?P<user_id>\d+)/$', views.admin_user_details, name='user-details'),
    url(r'^admin/user/(?P<user_id>\d+)/edit/$', views.admin_user_form, name='user-edit'),
    url(r'^admin/user/(?P<user_id>\d+)/delete/$', views.admin_user_delete, name='user-delete'),
]