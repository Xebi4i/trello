from django.conf.urls import patterns, url
from NBA_players import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
