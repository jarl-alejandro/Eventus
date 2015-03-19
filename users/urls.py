from django.conf.urls import patterns, include, url
from .views import ProfileView

urlpatterns = patterns('',

    url(r'^logout/$', "users.views.log_out", name='logout'),
    url(r'^login/', "users.views.log_in", name="login"),
    url(r'^registrate/', "users.views.registrate", name="registrate"),
    url(r'^profile/', ProfileView.as_view(), name="profile"),
    
)
