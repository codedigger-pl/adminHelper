# -*- coding: utf-8 -*-

from djangular.forms import NgModelFormMixin, NgModelForm, NgFormValidationMixin, NgForm
from djangular.styling.bootstrap3.forms import Bootstrap3FormMixin, Bootstrap3Form

from .models import PersonGroup, Person


class AngularPGroupAddForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
    """
    Form allowing manipulating person groups.
    """
    form_name = 'form'

    class Meta:
        model = PersonGroup
        fields = ('name', 'description')

class AngularPersonAddForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
    """
    Form allowing manipulating persons.
    """
    form_name = 'form'

    class Meta:
        model = Person
        fields = ('last_name', 'first_name', 'rank', 'card_number', 'group')
