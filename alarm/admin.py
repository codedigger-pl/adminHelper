#!/usr/bin/env python

# -*- coding: utf-8 -*-


from django.contrib import admin

from .models import AlarmConfirm, AlarmOrder, AlarmRequest, AlarmRule, AlarmZone

admin.site.register(AlarmZone)
admin.site.register(AlarmRule)
admin.site.register(AlarmRequest)
admin.site.register(AlarmOrder)
admin.site.register(AlarmConfirm)

