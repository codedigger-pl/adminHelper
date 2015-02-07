#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Person, PersonGroup


class DefPersonGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonGroup
        fields = ('id', 'name')


class DefPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'group', 'card_number', 'is_active')


class PersonSerializer(serializers.ModelSerializer):
    """ PersonSerializer

    Default Person serializer with all fields in string format
    """
    group = DefPersonGroupSerializer

    class Meta:
        model = Person
        fields = ('id', 'rank', 'first_name', 'last_name', 'group', 'card_number', 'is_active')


class MinimalPersonSerializer(serializers.ModelSerializer):
    """ PersonSerializer

    Person serializer with minimal information about person: first name, last name and group
    """
    group = serializers.StringRelatedField()

    class Meta:
        model = Person
        fields = ('id', 'rank', 'first_name', 'last_name', 'group')
