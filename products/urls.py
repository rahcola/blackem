from django.conf.urls.defaults import *
from django.views.generic import list_detail
from products.models import Product

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

info_dict = {
  'queryset': Product.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', list_detail.object_list, info_dict),
    (r'^(?P<object_id>\d+)$', list_detail.object_detail, info_dict),
)
