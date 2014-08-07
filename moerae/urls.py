from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'api/data', 'app.views.data'),
    url(r'catalog/data', 'app.views.catalogData'),
    url(r'^$', 'app.views.index'),
    url(r'^generate_catalog/$', 'app.views.generateCatalog'),
    url(r'^hostname/(?P<slug>[-\w]+)/$', 'app.views.hostname_page'),
    url(r'^admin/', include(admin.site.urls)),
)
