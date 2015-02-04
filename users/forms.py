#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.forms import ModelForm

from djangular.forms import NgFormValidationMixin, NgModelFormMixin

from .models import PersonGroup


class PersonGroupAddForm(NgModelFormMixin, ModelForm):
    class Meta:
        model = PersonGroup
        fields = ('name', 'description')