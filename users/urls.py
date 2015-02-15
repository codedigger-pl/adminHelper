# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from rest_framework.routers import DefaultRouter

from .views import UsersOverview, PersonAddView, PersonGroupAddView, PersonList, PersonDetail, PGroupList
from .views import PersonGroupViewset, PersonViewset


# TODO: move this to main API generating after finish
router = DefaultRouter()
router.register(r'personGroups', PersonGroupViewset)
router.register(r'persons', PersonViewset)

urlpatterns = patterns('',
    url(r'^overview', UsersOverview, name='usersOverview'),
    url(r'^person_list', PersonList.as_view(), name='person_list'),
    url(r'^person_detail', PersonDetail.as_view(), name='person_detail'),
    url(r'^personGroup_list', PGroupList.as_view(), name='pgroup_list'),
    url(r'^addPersonGroup', PersonGroupAddView.as_view(), name='add_personGroup'),
    url(r'^addPerson', PersonAddView.as_view(), name='add_person'),
)
