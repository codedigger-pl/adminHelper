#!/usr/bin/env python

# -*- coding: utf-8 -*-


from django.contrib import admin

from .models import ACSConfirm, ACSOrder, ACSRequest, ACSRule, ACSZone

admin.site.register(ACSZone)
admin.site.register(ACSRule)
admin.site.register(ACSRequest)
admin.site.register(ACSOrder)
admin.site.register(ACSConfirm)
