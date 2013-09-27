from django.conf.urls import patterns, include, url
from myblogapp.views import myview
from myblogapp.views import frontpage

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblogsite.views.home', name='home'),
    # url(r'^myblogsite/', include('myblogsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^myview/$',myview),
     url(r'^blog/$',frontpage),
)


