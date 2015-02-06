#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from djangular.forms import NgModelFormMixin, NgModelForm
from djangular.styling.bootstrap3.forms import Bootstrap3FormMixin

from .models import PersonGroup


class PersonGroupAddForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
    class Meta:
        model = PersonGroup
        fields = ('name', 'description')
