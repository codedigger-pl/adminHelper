# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

from .forms import (AngularPGroupAddForm,
                    AngularPersonAddForm, AngularPersonCardNumberForm, AngularPersonDataForm, AngularPersonPhotoForm,
                    AngularUserAddForm, )


class UserHomepage(TemplateView):
    """ Homepage view.

    Display homepage. Class based on TemplateView.
    :return: generated base.html
    """

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
        context = super(PersonDetail, self).get_context_data(**kwargs)
        context.update(cardNumberForm=AngularPersonCardNumberForm())
        context.update(dataForm=AngularPersonDataForm())
        context.update(photoForm=AngularPersonPhotoForm())
        return context


class PGroupList(TemplateView):
    """ Person group list view.

    Display list of person groups in system. Class based on TemplateView.
    :return: generated pgroupList.html
    """

    template_name = 'pgroupList.html'


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
        context = super(PersonGroupAddView, self).get_context_data(**kwargs)
        context.update(form=AngularPGroupAddForm())
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
        context = super(PersonAddView, self).get_context_data(**kwargs)
        context.update(form=AngularPersonAddForm())
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
        context = super(UserAddView, self).get_context_data(**kwargs)
        context.update(form=AngularUserAddForm())
        context.update(form_title='Dodaj użytkownika')
        return context
