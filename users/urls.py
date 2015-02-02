#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from .views import UsersOverview

# api
from .views import PersonGroupViewset, PersonViewset, personGroupAddForm
from .api import PersonDetail, PersonList, PersonGroupDetail, PersonGroupList

router = DefaultRouter()
router.register(r'personGroups', PersonGroupViewset)
router.register(r'persons', PersonViewset)

urlpatterns = patterns('',
    url(r'^overview', UsersOverview, name='usersOverview'),
    url(r'^addPersonGroup', personGroupAddForm.as_view(), name='add_personGroup'),
)
