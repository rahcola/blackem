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
    (r'^(?P<object_id>\d+)$', list_detail.object_detail, product_dict),
    (r'^categories/$', list_detail.object_list, category_dict),
    (r'^categories/(?P<object_id>\d+)$', list_detail.object_detail, category_dict),
)
