#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from djangular.forms import NgModelFormMixin, NgModelForm, NgFormValidationMixin, NgForm
from djangular.styling.bootstrap3.forms import Bootstrap3FormMixin, Bootstrap3Form

from .models import PersonGroup


class AngularPGroupAddForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
    form_name = 'form'

    class Meta:
        model = PersonGroup
        fields = ('name', 'description')
