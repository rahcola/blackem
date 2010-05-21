from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  (r'^admin/', include(admin.site.urls)),
  (r'^$', 'blackem.pantries.views.index'),
  (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
  (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html', 'next_page': '/'}),
  (r'^products/', include('blackem.products.urls')),
  (r'^pantries/', include('blackem.pantries.urls')),
)

