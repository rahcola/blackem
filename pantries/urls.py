from django.conf.urls.defaults import *

urlpatterns = patterns(
    'pantries.views',
    (r'^$', 'list'),
    (r'^(?P<pantry_id>\d+)$', 'detail'),
    (r'^new$', 'new'),
    (r'^delete/(?P<pantry_id>\d+)$', 'delete'),
    (r'^(?P<pantry_id>\d+)/add$', 'add_content'),
    (r'^(?P<pantry_id>\d+)/add/(?P<category_id>\d+)$', 'add_content'),
    (r'^(?P<pantry_id>\d+)/add/(?P<category_id>\d+)/(?P<product_id>\d+)$', 'add_content'),
    (r'^(?P<pantry_id>\d+)/delete/(?P<content_id>\d+)$', 'delete_content'),
)

