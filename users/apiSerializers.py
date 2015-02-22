# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Person, PersonGroup, SysUser


class DefPersonGroupSerializer(serializers.ModelSerializer):
    """
    Default person group serializer.
    """
    class Meta:
        model = PersonGroup
        fields = ('id', 'name', 'creation_date_date', 'creation_date_time', 'description')
        read_only_fields = ('id', 'creation_date_date', 'creation_date_time')


class DefPersonSerializer(serializers.ModelSerializer):
    """
    Default person serializer
    """

    group = DefPersonGroupSerializer

    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'rank', 'group', 'card_number', 'is_active', 'creation_date')
        read_only_fields = ('id', 'creation_date')


class DefUserSerializer(serializers.ModelSerializer):
    """
    Default person serializer
    """

    class Meta:
        model = SysUser
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'rank', 'email', )
        read_only_fields = ('id', 'password')


class UserPasswordSerializer(serializers.ModelSerializer):
    """
    Default user's password serializer
    """

    class Meta:
        model = SysUser
        fields = ('password', )


class PersonSerializer(serializers.ModelSerializer):
    """ PersonSerializer

    Default Person serializer used in API
    """
    group = DefPersonGroupSerializer

    class Meta:
        model = Person
        fields = ('id',
                  'rank',
                  'first_name',
                  'last_name',
                  'group',
                  'card_number',
                  'is_active',
                  'photo',
                  'creation_date_date',
                  'creation_date_time',)
        read_only_fields = ('id',
                            'creation_date_date',
                            'creation_date_time',)


class MinimalPersonSerializer(serializers.ModelSerializer):
    """ PersonSerializer

    Person serializer with minimal information about person: first name, last name and group
    """
    group = serializers.StringRelatedField()

    class Meta:
        model = Person
        fields = ('id', 'rank', 'first_name', 'last_name', 'group')
