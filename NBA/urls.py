from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'admin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('NBA.apps.base_site.urls')),
    url(r'^players/', include('NBA.apps.NBA_players.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
