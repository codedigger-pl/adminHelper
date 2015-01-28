#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Person, PersonGroup


class DefPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'firstName', 'lastName', 'group', 'cardNumber', 'isActive')


class PersonSerializer(serializers.ModelSerializer):
    """ PersonSerializer

    Default Person serializer with all fields in string format
    """
    group = serializers.StringRelatedField()

    class Meta:
        model = Person
        fields = ('id', 'firstName', 'lastName', 'group', 'cardNumber', 'isActive')


class DefPersonGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonGroup
        fields = ('id', 'name')
