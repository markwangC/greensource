from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'site_warehouse.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^admin/doc/",include("django.contrib.admindocs.urls")),
    url(r"^grappelli/",include("grappelli.urls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^warehouse/',include("warehouse.urls",namespace="warehouse")),

)
