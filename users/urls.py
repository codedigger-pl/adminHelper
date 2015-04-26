# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import (UsersOverview,
                    PersonAddView, PersonGroupAddView, UserAddView,
                    PersonList, PersonDetail,
                    PersonGroupList, PersonGroupDetail,
                    LoginForm, LoginView)

urlpatterns = patterns('',
    url(r'^overview', UsersOverview.as_view(), name='usersOverview'),
    url(r'^person_list', PersonList.as_view(), name='person_list'),
    url(r'^person_detail', PersonDetail.as_view(), name='person_detail'),
    url(r'^personGroup_list', PersonGroupList.as_view(), name='pgroup_list'),
    url(r'^personGroup_detail', PersonGroupDetail.as_view(), name='pgroup_detail'),
    url(r'^addPersonGroup', PersonGroupAddView.as_view(), name='add_personGroup'),
    url(r'^addPerson', PersonAddView.as_view(), name='add_person'),
    url(r'^addUser', UserAddView.as_view(), name='add_user'),
    url(r'^login_form', LoginForm.as_view(), name='login_form'),
    url(r'^login', LoginView.as_view(), name='login_view'),
)
