# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import ACSZone, ACSOrder, ACSRule, ACSRequest


class ACSZoneSerializer(serializers.ModelSerializer):
    """Default ACS zone serializer"""

    class Meta:
        model = ACSZone
        fields = ('id', 'name', 'description', 'creation_date_date', 'creation_date_time', 'manager')
        read_only_fields = ('id', 'creation_date_date', 'creation_date_time')


class ListACSZoneSerializer(serializers.ModelSerializer):
    """ACS zone serializer used to list zones"""

    manager = serializers.StringRelatedField()

    class Meta:
        model = ACSZone
        fields = ('id', 'name', 'description', 'manager', 'persons_count')
        read_only_fields = ('id')


class ACSRuleSerializer(serializers.ModelSerializer):
    """Default ACS rule serializer"""

    class Meta:
        model = ACSRule
        fields = ('id', 'person', 'zone', 'confirmed', 'creation_date_date', 'creation_date_time')
        read_only_fields = ('id', 'confirmed', 'creation_date_date', 'creation_date_time')


class ACSOrderSerializer(serializers.ModelSerializer):
    """Default ACS order serializer"""

    class Meta:
        model = ACSOrder
        fields = ('id', 'user', 'grant_privilege', 'creation_date_date', 'creation_date_time', 'rule')
        read_only_fields = ('id', 'creation_date_date', 'creation_date_time')


class ListACSOrderSerializer(serializers.ModelSerializer):
    """ACS order serializer used in lists"""

    rule_zone = serializers.ReadOnlyField(source='rule.zone.name')
    rule_person = serializers.StringRelatedField(source='rule.person')

    class Meta:
        model = ACSOrder
        fields = ('id', 'user', 'grant_privilege', 'rule_zone', 'rule_person')
        read_only_fields = ('id', )


class ACSRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ACSRequest
        fields = ('id', 'creation_date_date', 'creation_date_time', 'user', 'rule', 'grant_privilege')
        read_only_fields = ('id', 'creation_date_date', 'creation_date_time')


class ListACSRequestSerializer(serializers.ModelSerializer):

    rule_zone = serializers.ReadOnlyField(source='rule.zone.name')
    rule_person = serializers.StringRelatedField(source='rule.person')
    user = serializers.StringRelatedField()

    class Meta:
        model = ACSRequest
        fields = ('id', 'user', 'rule_zone', 'rule_person', 'grant_privilege')
        read_only_fields = ('id', )
