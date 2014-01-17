from django.conf.urls import patterns, url
from NBA.apps.base_site import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
