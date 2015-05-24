# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Key, KeyOrder, KeyRule, KeyRequest


class KeySerializer(serializers.ModelSerializer):
    """Default Key zone serializer"""

    class Meta:
        model = Key
        fields = ('id', 'name', 'description', 'creation_date_date', 'creation_date_time', 'manager')
        read_only_fields = ('id', 'creation_date_date', 'creation_date_time')


class ListKeySerializer(serializers.ModelSerializer):
    """Key zone serializer used to list zones"""

    manager = serializers.StringRelatedField()

    class Meta:
        model = Key
        fields = ('id', 'name', 'description', 'manager', 'persons_count')
        read_only_fields = ('id')


class KeyRuleSerializer(serializers.ModelSerializer):
    """Default Key rule serializer"""

    class Meta:
        model = KeyRule
        fields = ('id', 'person', 'key', 'confirmed', 'creation_date_date', 'creation_date_time')
        read_only_fields = ('id', 'confirmed', 'creation_date_date', 'creation_date_time')


class KeyOrderSerializer(serializers.ModelSerializer):
    """Default Key order serializer"""

    class Meta:
        model = KeyOrder
        fields = ('id', 'user', 'grant_privilege', 'creation_date_date', 'creation_date_time', 'rule')
        read_only_fields = ('id', 'creation_date_date', 'creation_date_time')


class ListKeyOrderSerializer(serializers.ModelSerializer):
    """Key order serializer used in lists"""

    rule_key = serializers.ReadOnlyField(source='rule.key.name')
    rule_person = serializers.StringRelatedField(source='rule.person')

    class Meta:
        model = KeyOrder
        fields = ('id', 'user', 'grant_privilege', 'rule_key', 'rule_person')
        read_only_fields = ('id', )


class KeyRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = KeyRequest
        fields = ('id', 'creation_date_date', 'creation_date_time', 'user', 'rule', 'grant_privilege')
        read_only_fields = ('id', 'creation_date_date', 'creation_date_time')


class ListKeyRequestSerializer(serializers.ModelSerializer):

    rule_key = serializers.ReadOnlyField(source='rule.key.name')
    rule_person = serializers.StringRelatedField(source='rule.person')
    user = serializers.StringRelatedField()

    class Meta:
        model = KeyRequest
        fields = ('id', 'user', 'rule_key', 'rule_person', 'grant_privilege')
        read_only_fields = ('id', )
