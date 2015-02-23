# -*- coding: utf-8 -*-

from djangular.forms import NgModelFormMixin, NgModelForm, NgFormValidationMixin, NgForm
from djangular.styling.bootstrap3.forms import Bootstrap3FormMixin, Bootstrap3Form

from .models import PersonGroup, Person, SysUser


class AngularPGroupAddForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
    """
    Form allowing manipulating person groups.
    """
    form_name = 'pgroupAddForm'

    class Meta:
        model = PersonGroup
        fields = ('name', 'description')


class AngularPersonAddForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
    """
    Form allowing manipulating persons.
    """
    form_name = 'personAddForm'

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


class AngularPersonPhotoForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
    """
    Form allowing change person photo.
    """
    form_name = 'personPhotoForm'

    class Meta:
        model = Person
        fields = ('photo', )

    def __init__(self, *args, **kwargs):
        kwargs.update(scope_prefix='person')
        super(AngularPersonPhotoForm, self).__init__(*args, **kwargs)


class AngularUserAddForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
    """
    Form allowing change person photo.
    """
    form_name = 'userAddForm'

    class Meta:
        model = SysUser
        fields = ('username', 'first_name', 'last_name', 'rank', 'email' )

    def __init__(self, *args, **kwargs):
        kwargs.update(scope_prefix='user')
        super(AngularUserAddForm, self).__init__(*args, **kwargs)
