from django.conf.urls import patterns, url
from django.conf.urls.defaults import *
from api import router
import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.

urlpatterns = patterns('',
                       url(r'^puppet/(?P<hostname>.*)$',
                           views.puppet,
                           name='puppet'),
                       url(r'^walkit/(?P<hostname>.*)$',
                           views.walkit,
                           name='walkit'),
                       url(r'^workit/(?P<hostname>.*)$',
                           views.workit,
                           name='workit'),
                       url(r'^classworkit/(?P<hostname>.*)$',
                           views.classworkit,
                           name='classworkit'),
                       url(r'^optworkit/(?P<hostname>.*)$',
                           views.optworkit,
                           name='optworkit'),
                       url(r'^api-auth/',
                           include('rest_framework.urls',
                                   namespace='rest_framework')
                           ),
                       url(r'^',
                           include(router.urls)),
                       )
