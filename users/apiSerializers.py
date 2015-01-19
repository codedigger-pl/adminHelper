#!/usr/bin/env python

# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Person, PersonGroup, SysUser

class DefPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'firstName', 'lastName', 'cardNumber', 'isActive')

class DefPersonGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonGroup
        fields = ('id', 'name')

