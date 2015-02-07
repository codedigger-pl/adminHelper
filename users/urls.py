# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from rest_framework.routers import DefaultRouter

from .views import UsersOverview, PersonAddView, PersonGroupAddView
from .views import PersonGroupViewset, PersonViewset


# TODO: move this to main API generating after finish
router = DefaultRouter()
router.register(r'personGroups', PersonGroupViewset)
router.register(r'persons', PersonViewset)

urlpatterns = patterns('',
    url(r'^overview', UsersOverview, name='usersOverview'),
    url(r'^addPersonGroup', PersonGroupAddView.as_view(), name='add_personGroup'),
    url(r'^addPerson', PersonAddView.as_view(), name='add_person'),
)
