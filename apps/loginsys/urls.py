__author__ = 'artem'
from django.conf.urls import patterns, include, url
from apps.loginsys.views import *
urlpatterns = patterns('',

    url(r'^login/', login),
    url(r'^logout/', logout),
    url(r'^register/', register)





)
