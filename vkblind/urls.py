# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

import ims.urls
import feeds.urls
from views import login, logout, index


urlpatterns = patterns('',
    url('^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    url(r'^im/', include(ims.urls)),
    url(r'^feed/', include(feeds.urls)),
    url('', include('social.apps.django_app.urls', namespace='social'))
)
