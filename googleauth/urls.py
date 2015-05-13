try:
    from django.conf.urls import *
except:
    # django 1.3
    from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^login/$', 'googleauth.views.login', name='googleauth_login'),
    url(r'^callback/$', 'googleauth.views.callback', name='googleauth_callback'),
    url(r'^logout/$', 'googleauth.views.logout', name='googleauth_logout'),
)
