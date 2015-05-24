#!/usr/bin/env python

# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import KeyConfirm, KeyOrder, KeyRequest, KeyRule, Key

admin.site.register(Key)
admin.site.register(KeyRule)
admin.site.register(KeyRequest)
admin.site.register(KeyOrder)
admin.site.register(KeyConfirm)
