from django.conf.urls.defaults import *
from django.contrib.auth.forms import UserCreationForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'blackem.users.views.home'),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html', 'next_page': '/'}),
    (r'^register/$', 'django.views.generic.create_update.create_object',
        {'form_class': UserCreationForm,
         'post_save_redirect': '/'}),
    (r'^products/', include('blackem.products.urls')),
    (r'^pantries/', include('blackem.pantries.urls')),
)

