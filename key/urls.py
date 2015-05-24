# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import KeyOverview, AddKeyForm, AddKeyOrderForm, AddKeyRequestForm

urlpatterns = patterns('',
    url(r'^overview', KeyOverview.as_view(), name='keyOverview'),
    url(r'^addKeyOrder', AddKeyOrderForm.as_view(), name='add_keyOrder'),
    url(r'^addKeyRequest', AddKeyRequestForm.as_view(), name='add_keyRequest'),
    url(r'^addKey', AddKeyForm.as_view(), name='add_key'),
)
