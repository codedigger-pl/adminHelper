# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

from .models import PersonGroup, Person, SysUser
from .forms import (AngularPGroupAddForm,
                    AngularPersonAddForm, AngularPersonCardNumberForm, AngularPersonDataForm, AngularPersonPhotoForm,
                    AngularUserAddForm, )
from .filters import PersonFilter

from .apiSerializers import DefPersonGroupSerializer, PersonSerializer, MinimalPersonSerializer
from .apiSerializers import DefUserSerializer, UserPasswordSerializer


class UserHomepage(TemplateView):

    """ Homepage view.

    Display homepage. Class based on TemplateView.
    :return: generated base.html
    """

    template_name = 'base.html'


def UsersOverview(request):

    """ Users overview view.

    Generate part of main page containing all overview information about persons, person groups and users.
    Give access to adding persons, etc...
    :param request: request
    :return: generated Users overview page based on usersOverview.html template
    """

    resp = {}

    # getting objects counts
    # TODO: do this with API call and change view to TemplateView
    resp['personsCount'] = Person.objects.count()
    resp['groupsCount'] = PersonGroup.objects.count()

    # getting last registered objects
    # TODO: do this with API call and change view to TemplateView
    lastRegisteredPerson = Person.objects.last()
    if lastRegisteredPerson is not None:
        resp['lastRegisteredPerson'] = lastRegisteredPerson.last_name + ' ' + lastRegisteredPerson.first_name
    lastRegisteredGroup = PersonGroup.objects.last()
    if lastRegisteredGroup is not None:
        resp['lastRegisteredGroup'] = lastRegisteredGroup.name

    # return prepared data
    return render(request, 'usersOverview.html', resp)


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


class PersonGroupViewset(viewsets.ModelViewSet):
    """
    Person API viewset.

    """
    queryset = PersonGroup.objects.all()
    serializer_class = DefPersonGroupSerializer

    def list(self, request, *args, **kwargs):
        """
        Return person groups list based on params.

        :param request: request
        :param args: not used
        :param kwargs: dictionary can be:
            onlyLastItems: {int} - how many last items return
        :return: list of person groups based on params
        """

        queryset = PersonGroup.objects.all()

        if 'onlyLastItems' in request.QUERY_PARAMS:
            lastItems = int(request.QUERY_PARAMS['onlyLastItems'])
            startIndex = 0 if queryset.count() - lastItems < 0 else queryset.count() - lastItems
            queryset = queryset[startIndex:]

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class PersonViewset(viewsets.ModelViewSet):
    """Person viewset

    Defines API all methods to Person"""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_class = PersonFilter

    def list(self, request, *args, **kwargs):
        """
        Return person list based on params.
        :param request: request
        :param args: not used
        :param kwargs: dictionary can be:
            modelType: 'minimal' - return minimal information about persons
            onlyLastItems: {int} - how many last items return
        :return: list of persons based on params
        """

        queryset = self.filter_queryset(self.get_queryset())

        if 'modelType' in request.QUERY_PARAMS:
            if request.QUERY_PARAMS['modelType'] == 'minimal':
                self.serializer_class = MinimalPersonSerializer

        if 'onlyLastItems' in request.QUERY_PARAMS:
            lastItems = int(request.QUERY_PARAMS['onlyLastItems'])
            startIndex = 0 if queryset.count() - lastItems < 0 else queryset.count() - lastItems
            queryset = queryset[startIndex:]

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class UserViewset(viewsets.ModelViewSet):
    """User viewset

    Defines API all methods to User"""
    queryset = SysUser.objects.all()
    serializer_class = DefUserSerializer

    @detail_route(methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = UserPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'hasło zmienione'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


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
