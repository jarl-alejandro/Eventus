from django.conf.urls import patterns, include, url
from .views import InicioView, AppView

urlpatterns = patterns('',
    url(r'^$', InicioView.as_view(), name="inicio"),
    url(r'^app/$', AppView.as_view(), name="app"),
)
