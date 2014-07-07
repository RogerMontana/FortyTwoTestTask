from django.conf.urls import patterns, include, url
from apps.hello.views import show_info_all, get_messages,show_info, settings, main

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



    url(r'^messages/', get_messages),

    url(r'^task/info_all/', show_info_all),
    url(r'^task/info/(?P<id>\d+)/$', show_info),
    url(r'^task/settings/', settings),
    url(r'^', main),


)