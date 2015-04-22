# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import AlarmOverview, AddAlarmZoneForm, AddAlarmOrderForm, AddAlarmRequestForm

urlpatterns = patterns('',
    url(r'^overview', AlarmOverview.as_view(), name='alarmOverview'),
    url(r'^addAlarmZone', AddAlarmZoneForm.as_view(), name='add_alarmZone'),
    url(r'^addAlarmOrder', AddAlarmOrderForm.as_view(), name='add_alarmOrder'),
    url(r'^addAlarmRequest', AddAlarmRequestForm.as_view(), name='add_alarmRequest'),
    # url(r'^personGroup_detail', PersonGroupDetail.as_view(), name='pgroup_detail'),
    # url(r'^addPersonGroup', PersonGroupAddView.as_view(), name='add_personGroup'),
    # url(r'^addPerson', PersonAddView.as_view(), name='add_person'),
    # url(r'^addUser', UserAddView.as_view(), name='add_user'),
)
