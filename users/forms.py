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
        fields = ('last_name', 'first_name', 'rank', 'card_number', 'group', 'photo')


class AngularPersonCardNumberForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
    """
    Form allowing change person card number.
    """
    form_name = 'cardNumberForm'

    class Meta:
        model = Person
        fields = ('card_number', )

    def __init__(self, *args, **kwargs):
        kwargs.update(scope_prefix='person')
        super(AngularPersonCardNumberForm, self).__init__(*args, **kwargs)


class AngularPersonDataForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
    """
    Form allowing change person data.
    """
    form_name = 'personDataForm'

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'rank', 'group')

    def __init__(self, *args, **kwargs):
        kwargs.update(scope_prefix='person')
        super(AngularPersonDataForm, self).__init__(*args, **kwargs)