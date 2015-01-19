#!/usr/bin/env python

# -*- coding: utf-8 -*-

from rest_framework import generics, mixins

from .models import PersonGroup, Person, SysUser
from .apiSerializers import DefPersonGroupSerializer

class PersonGroupList(generics.ListCreateAPIView):
    queryset = PersonGroup.objects.all()
    serializer_class = DefPersonGroupSerializer

class PersonGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonGroup.objects.all()
    serializer_class = DefPersonGroupSerializer