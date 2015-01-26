#!/usr/bin/env python

# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from rest_framework.routers import DefaultRouter

from .views import UserHomepage

# api
from .views import PersonGroupViewset, PersonViewset
from .api import PersonDetail, PersonList, PersonGroupDetail, PersonGroupList

router = DefaultRouter()
router.register(r'personGroups', PersonGroupViewset)
router.register(r'persons', PersonViewset)

urlpatterns = patterns('',
    url(r'^$', UserHomepage.as_view(), name='usersHomepage'),
    url(r'^api/', include(router.urls))
)
