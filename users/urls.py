from django.conf.urls import patterns, include, url
urlpatterns = patterns('',

    url(r'^logout/$', "users.views.log_out", name='logout'),
    url(r'^login/', "users.views.log_in", name="login"),
    url(r'^registrate/', "users.views.registrate", name="registrate"),
    
)
