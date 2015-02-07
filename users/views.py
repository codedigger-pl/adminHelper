#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from rest_framework import viewsets
from rest_framework.response import Response

from .models import PersonGroup, Person, SysUser
from .forms import AngularPGroupAddForm, AngularPersonAddForm
from .apiSerializers import DefPersonGroupSerializer, PersonSerializer, MinimalPersonSerializer


class UserHomepage(TemplateView):
    template_name = 'base.html'


def UsersOverview(request):
    resp = {}
    resp['personsCount'] = Person.objects.count()
    resp['groupsCount'] = PersonGroup.objects.count()

    lastRegisteredPerson = Person.objects.last()
    if lastRegisteredPerson is not None:
        resp['lastRegisteredPerson'] = lastRegisteredPerson.last_name + ' ' + lastRegisteredPerson.first_name

    lastRegisteredGroup = PersonGroup.objects.last()
    if lastRegisteredGroup is not None:
        resp['lastRegisteredGroup'] = lastRegisteredGroup.name

    return render(request, 'usersOverview.html', resp)


class PersonGroupViewset(viewsets.ModelViewSet):
    queryset = PersonGroup.objects.all()
    serializer_class = DefPersonGroupSerializer

    def list(self, request, *args, **kwargs):

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

    def list(self, request, *args, **kwargs):

        queryset = Person.objects.all()

        if 'modelType' in request.QUERY_PARAMS:
            if request.QUERY_PARAMS['modelType'] == 'minimal':
                self.serializer_class = MinimalPersonSerializer

        if 'onlyLastItems' in request.QUERY_PARAMS:
            lastItems = int(request.QUERY_PARAMS['onlyLastItems'])
            startIndex = 0 if queryset.count() - lastItems < 0 else queryset.count() - lastItems
            queryset = queryset[startIndex:]

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class PersonGroupAddView(TemplateView):
    template_name = 'personGroupAddForm.html'

    def get_context_data(self, **kwargs):
        context = super(PersonGroupAddView, self).get_context_data(**kwargs)
        context.update(form=AngularPGroupAddForm())
        return context


class PersonAddView(TemplateView):
    template_name = 'defaultForm.html'

    def get_context_data(self, **kwargs):
        context = super(PersonAddView, self).get_context_data(**kwargs)
        context.update(form=AngularPersonAddForm())
        context.update(form_title='Dodaj pracownika')
        return context