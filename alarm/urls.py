# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import AlarmOverview, AddAlarmZoneForm

urlpatterns = patterns('',
    url(r'^overview', AlarmOverview.as_view(), name='alarmOverview'),
    url(r'^addAlarmZone', AddAlarmZoneForm.as_view(), name='add_alarmZone'),
    # url(r'^person_detail', PersonDetail.as_view(), name='person_detail'),
    # url(r'^personGroup_list', PersonGroupList.as_view(), name='pgroup_list'),
    # url(r'^personGroup_detail', PersonGroupDetail.as_view(), name='pgroup_detail'),
    # url(r'^addPersonGroup', PersonGroupAddView.as_view(), name='add_personGroup'),
    # url(r'^addPerson', PersonAddView.as_view(), name='add_person'),
    # url(r'^addUser', UserAddView.as_view(), name='add_user'),
)
