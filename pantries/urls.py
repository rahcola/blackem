from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blackem.pantries.views',
    (r'^$', 'index'),
    (r'^(?P<pantry_id>\d+)$', 'show'),
)

