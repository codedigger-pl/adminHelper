#!/usr/bin/env python

# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from .views import UserHomepage

urlpatterns = patterns('',
    url(r'^$', UserHomepage.as_view(), name='usersHomepage'),
)
