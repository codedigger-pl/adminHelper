# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

from djangular.forms import NgModelFormMixin, NgModelForm
from djangular.styling.bootstrap3.forms import Bootstrap3FormMixin

from .models import Person, PersonGroup, SysUser


class UserHomepage(TemplateView):
    """Shows homepage"""
    template_name = 'base.html'


class UsersOverview(TemplateView):
    """ Users overview view.

    Generate part of main page containing all overview information about persons, person groups and users.
    Give access to adding persons, etc...
    :return: generated Users overview page based on usersOverview.html template
    """
    template_name = 'usersOverview.html'


class PersonList(TemplateView):
    """ Person list view.

    Display list of persons in all systems. Class based on TemplateView.
    :return: generated personList.html
    """

    template_name = 'personList.html'


class PersonDetail(TemplateView):
    """ Person detail view.

    Display persons detail info. Class based on TemplateView.
    :return: generated personDetail.html
    """
    template_name = 'personDetail.html'

    def get_context_data(self, **kwargs):
        """
        Return generated context data used to generating template. Added fields:
          cardNumberForm: form allowing change person's card number
          dataForm: form allowing change person's data
          photoForm: form allowing change person's photo
        :param kwargs:
        :return: generated context data
        """
        class CardNumberAngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            form_name = 'cardNumberForm'

            class Meta:
                model = Person
                fields = ('card_number', )

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='person')
                super(CardNumberAngularForm, self).__init__(*args, **kwargs)

        class DataAngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            form_name = 'personDataForm'

            class Meta:
                model = Person
                fields = ('first_name', 'last_name', 'rank', 'group')

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='person')
                super(DataAngularForm, self).__init__(*args, **kwargs)

        class PhotoAngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            form_name = 'personPhotoForm'

            class Meta:
                model = Person
                fields = ('photo', )

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='person')
                super(PhotoAngularForm, self).__init__(*args, **kwargs)

        context = super(PersonDetail, self).get_context_data(**kwargs)
        context.update(cardNumberForm=CardNumberAngularForm())
        context.update(dataForm=DataAngularForm())
        context.update(photoForm=PhotoAngularForm())
        return context


class PersonGroupList(TemplateView):
    """ Person group list view.

    Display list of person groups in system. Class based on TemplateView.
    :return: generated pgroupList.html
    """
    template_name = 'pgroupList.html'


class PersonGroupDetail(TemplateView):
    """ Person group detail view.

    Display selected person group details.
    :return: generated pgroupDetail.html
    """
    template_name = 'pgroupDetail.html'

    def get_context_data(self, **kwargs):
        """
        Return generated context data used to generating template. Added fields:
          cardNumberForm: form allowing change person's card number
          dataForm: form allowing change person's data
          photoForm: form allowing change person's photo
        :param kwargs:
        :return: generated context data
        """
        class AngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            form_name = 'personGroupForm'

            class Meta:
                model = PersonGroup
                fields = ('name', 'description')

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='personGroup')
                super(AngularForm, self).__init__(*args, **kwargs)

        context = super(PersonGroupDetail, self).get_context_data(**kwargs)
        context.update(personGroupForm=AngularForm)
        return context


class PersonGroupAddView(TemplateView):
    """
    Template view used for generating form to add person groups.
    """
    template_name = 'defaultForm.html'

    def get_context_data(self, **kwargs):
        """
        Return generated context data used to generating template. Added fields:
          form: what form to generate
          form_title: form title
        :param kwargs:
        :return: generated context data
        """
        class AngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            form_name = 'pgroupAddForm'

            class Meta:
                model = PersonGroup
                fields = ('name', 'description')

        context = super(PersonGroupAddView, self).get_context_data(**kwargs)
        context.update(form=AngularForm())
        context.update(form_title='Dodaj grupę pracowników')
        return context


class PersonAddView(TemplateView):
    """
    Template view used for generating form to add persons
    """
    template_name = 'defaultForm.html'

    def get_context_data(self, **kwargs):
        """
        Return generated context data used to generating template. Added fields:
          form: what form to generate
          form title: form title
        :param kwargs:
        :return: generated context data
        """
        class AngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            form_name = 'personAddForm'

            class Meta:
                model = Person
                fields = ('last_name', 'first_name', 'rank', 'card_number', 'group', 'photo')

        context = super(PersonAddView, self).get_context_data(**kwargs)
        context.update(form=AngularForm())
        context.update(form_title='Dodaj pracownika')
        return context


class UserAddView(TemplateView):
    """
    Template view used for generating form to add persons
    """
    template_name = 'defaultForm.html'

    def get_context_data(self, **kwargs):
        """
        Return generated context data used to generating template. Added fields:
          form: what form to generate
          form title: form title
        :param kwargs:
        :return: generated context data
        """
        class AngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            form_name = 'userAddForm'

            class Meta:
                model = SysUser
                fields = ('username', 'first_name', 'last_name', 'rank', 'email')

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='user')
                super(AngularForm, self).__init__(*args, **kwargs)

        context = super(UserAddView, self).get_context_data(**kwargs)
        context.update(form=AngularForm())
        context.update(form_title='Dodaj użytkownika')
        return context


class LoginForm(TemplateView):
    """Login to system form"""
    template_name = 'defaultForm.html'

    def get_context_data(self, **kwargs):
        class AngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            form_name = 'loginForm'

            class Meta:
                model = SysUser
                fields = ('username', 'password')

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='login')
                super(AngularForm, self).__init__(*args, **kwargs)

        context = super(LoginForm, self).get_context_data(**kwargs)
        context.update(form=AngularForm())
        context.update(form_title='Logowanie do systemu')
        return context
