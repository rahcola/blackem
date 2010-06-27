from django.conf.urls.defaults import *
from django.views.generic import list_detail
from products.models import Product, Category

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

product_dict = {
    'queryset': Product.objects.all(),
}
category_dict = {
    'queryset': Category.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', list_detail.object_list, product_dict),
    (r'^(?P<object_id>\d+)$', 'products.views.detail_product'),
    (r'^new/$', 'products.views.new_product'),
    (r'^(?P<object_id>\d+)/delete$', 'products.views.delete_product'),
    (r'^(?P<object_id>\d+)/change$', 'products.views.change_product'),
    (r'^categories/$', list_detail.object_list, category_dict),
    (r'^categories/new$', 'products.views.new_category'),
    (r'^categories/(?P<object_id>\d+)$', 'products.views.detail_category'),
    (r'^categories/(?P<object_id>\d+)/delete$',
     'products.views.delete_category'),
)
