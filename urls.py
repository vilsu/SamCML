from django.conf.urls.defaults import *
# Import all methods which create content here
from views import my_homepage_view 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^$', my_homepage_view),

    # Example:
    # (r'^SamCML/', include('SamCML.foo.urls')),

    # TODO auth
#    (r'^openid/$', 'SamCML.openid.openid_form'),
#    (r'^openid/process/(?P<token>.*)/$', 'SamCML.openid.process'),

    (r'^admin/code/report/$', 'code.admin_views.report'),  # may be unnecessary
    (r'^admin/', include('django.contrib.admin.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^comments/', include('django.contrib.comments.urls')),
)
