from django.conf.urls.defaults import *

urlpatterns = patterns(
    'shoppinglists.views',
    (r'^(?P<shoppinglist_id>\d+)$', 'detail'),
    (r'^new$', 'new'),
    (r'^delete/(?P<shoppinglist_id>\d+)$', 'delete'),
    (r'^(?P<shoppinglist_id>\d+)/add$', 'add_item'),
    (r'^(?P<shoppinglist_id>\d+)/add/(?P<category_id>\d+)$', 'add_item'),
    (r'^(?P<shoppinglist_id>\d+)/add/(?P<category_id>\d+)/(?P<product_id>\d+)$',
     'add_item'),
    (r'^(?P<shoppinglist_id>\d+)/delete/(?P<item_id>\d+)$', 'delete_item'),
)

