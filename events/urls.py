from django.conf.urls import patterns, include, url
from .views import InicioView, AppView, CreateEventView, EventDetailView

urlpatterns = patterns('',
    url(r'^$', InicioView.as_view(), name="inicio"),
    url(r'^app/$', AppView.as_view(), name="app"),
    url(r'^crear/evento/$', CreateEventView.as_view(), name="crear"),
    url(r'^evento/(?P<slug>[-\w]+)$', EventDetailView.as_view(), name="detail"),
)