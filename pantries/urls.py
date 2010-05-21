from django.conf.urls.defaults import *

urlpatterns = patterns('pantries.views',
    (r'^$', 'index'),
    (r'^(?P<pantry_id>\d+)$', 'show'),
)

