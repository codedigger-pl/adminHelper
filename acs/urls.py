# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import ACSOverview, AddACSZoneForm, AddACSOrderForm, AddACSRequestForm

urlpatterns = patterns('',
    url(r'^overview', ACSOverview.as_view(), name='ACSOverview'),
    url(r'^addACSZone', AddACSZoneForm.as_view(), name='add_ACSZone'),
    url(r'^addACSOrder', AddACSOrderForm.as_view(), name='add_ACSOrder'),
    url(r'^addACSRequest', AddACSRequestForm.as_view(), name='add_ACSRequest'),
    # url(r'^personGroup_detail', PersonGroupDetail.as_view(), name='pgroup_detail'),
    # url(r'^addPersonGroup', PersonGroupAddView.as_view(), name='add_personGroup'),
    # url(r'^addPerson', PersonAddView.as_view(), name='add_person'),
    # url(r'^addUser', UserAddView.as_view(), name='add_user'),
)
