from django.conf.urls.defaults import *
from pantries.models import Pantry

urlpatterns = patterns(
    'pantries.views',
    (r'^$', 'index'),
    (r'^(?P<pantry_id>\d+)$', 'show'),
    (r'^new/$', 'new'),
)

