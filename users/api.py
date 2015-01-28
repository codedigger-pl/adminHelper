#!/usr/bin/env python
# -*- coding: utf-8 -*-


from rest_framework import generics

from .models import PersonGroup, Person
from .apiSerializers import DefPersonGroupSerializer, PersonSerializer


class PersonGroupList(generics.ListCreateAPIView):
    queryset = PersonGroup.objects.all()
    serializer_class = DefPersonGroupSerializer


class PersonGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonGroup.objects.all()
    serializer_class = DefPersonGroupSerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
