# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import SysUser, Person, PersonGroup

admin.site.register(SysUser)

admin.site.register(Person)
admin.site.register(PersonGroup)
