#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.forms import ModelForm

from djangular.forms import NgModelFormMixin, NgModelForm

from crispy_forms.helper import FormHelper

from .models import PersonGroup


class PersonGroupAddForm(NgModelFormMixin, NgModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonGroupAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'

    class Meta:
        model = PersonGroup
        fields = ('name', 'description')
