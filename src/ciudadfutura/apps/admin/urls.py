from django.conf.urls import url
from . import views

urlpatterns = [

    # Admin urls
    url(r'^admin/$', views.admin_dashboard, name='dashboard'),

    # Tags urls
    url(r'^admin/tag/$', views.admin_tag_list, name='tag-list'),
    url(r'^admin/tag/create/$', views.admin_tag_form, name='tag-create'),
    url(r'^admin/tag/(?P<tag_id>\d+)/edit/$', views.admin_tag_form, name='tag-edit'),
    url(r'^admin/tag/(?P<tag_id>\d+)/delete/$', views.admin_tag_delete, name='tag-delete'),

    # User urls
    url(r'^admin/user/$', views.admin_user_list, name='user-list'),
    url(r'^admin/user/create/$', views.admin_user_form, name='user-create'),
    url(r'^admin/user/(?P<user_id>\d+)/$', views.admin_user_details, name='user-details'),
    url(r'^admin/user/(?P<user_id>\d+)/edit/$', views.admin_user_edit, name='user-edit'),
    url(r'^admin/user/(?P<user_id>\d+)/delete/$', views.admin_user_delete, name='user-delete'),

    # Product urls
    url(r'^admin/product/$', views.admin_product_list, name='product-list'),
    url(r'^admin/product/create/$', views.admin_product_form, name='product-create'),
    url(r'^admin/product/(?P<product_id>\d+)/edit/$', views.admin_product_form, name='product-edit'),
    url(r'^admin/product/(?P<product_id>\d+)/delete/$', views.admin_product_delete, name='product-delete'),

    # Category urls
    url(r'^admin/category/$', views.admin_category_list, name='category-list'),
    url(r'^admin/category/create/$', views.admin_category_form, name='category-create'),
    url(r'^admin/category/(?P<category_id>\d+)/edit/$', views.admin_category_form, name='category-edit'),
    url(r'^admin/category/(?P<category_id>\d+)/delete/$', views.admin_category_delete, name='category-delete'),

    # Supplier urls
    url(r'^admin/supplier/$', views.admin_supplier_list, name='supplier-list'),
    url(r'^admin/supplier/create/$', views.admin_supplier_form, name='supplier-create'),
    url(r'^admin/supplier/(?P<supplier_id>\d+)/edit/$', views.admin_supplier_form, name='supplier-edit'),
    url(r'^admin/supplier/(?P<supplier_id>\d+)/delete/$', views.admin_supplier_delete, name='supplier-delete'),

    # Circle urls
    url(r'^admin/circle/$', views.admin_circle_list, name='circle-list'),
    url(r'^admin/circle/create/$', views.admin_circle_form, name='circle-create'),
    url(r'^admin/circle/(?P<circle_id>\d+)/edit/$', views.admin_circle_form, name='circle-edit'),
    url(r'^admin/circle/(?P<circle_id>\d+)/delete/$', views.admin_circle_delete, name='circle-delete'),

    # ShoppingCycle urls
    url(r'^admin/shopping/$', views.admin_shopping_cycle_list, name='shopping-cycle-list'),
    url(r'^admin/shopping/create/$', views.admin_shopping_cycle_form, name='shopping-cycle-create'),
    url(r'^admin/shopping/(?P<shopping_cycle_id>\d+)/edit/$', views.admin_shopping_cycle_form, name='shopping-cycle-edit'),
    url(r'^admin/shopping/(?P<shopping_cycle_id>\d+)/delete/$', views.admin_shopping_cycle_delete, name='shopping-cycle-delete'),

    # Order urls
    url(r'^admin/order/$', views.admin_order_list, name='order-list'),
    url(r'^admin/order/create/$', views.admin_order_form, name='order-create'),
    url(r'^admin/order/(?P<order_id>\d+)/edit/$', views.admin_order_form, name='order-edit'),
    url(r'^admin/order/(?P<order_id>\d+)/delete/$', views.admin_order_delete, name='order-delete'),
    url(r'^admin/order/(?P<order_id>\d+)/details/$', views.admin_order_details, name='order-details'),

]
