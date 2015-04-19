# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import AlarmZone, AlarmOrder, AlarmRule


class AlarmZoneSerializer(serializers.ModelSerializer):
    """Default alarm zone serializer"""

    class Meta:
        model = AlarmZone
        fields = ('id', 'name', 'description', 'creation_date_date', 'creation_date_time', 'manager')
        read_only_fields = ('id', 'creation_date_date', 'creation_date_time')


class ListAlarmZoneSerializer(serializers.ModelSerializer):
    """Alarm zone serializer used to list zones"""

    manager = serializers.StringRelatedField()

    class Meta:
        model = AlarmZone
        fields = ('id', 'name', 'description', 'manager')
        read_only_fields = ('id')


class AlarmRuleSerializer(serializers.ModelSerializer):
    """Default alarm rule serializer"""

    class Meta:
        model = AlarmRule
        fields = ('id', 'person', 'zone', 'confirmed', 'creation_date_date', 'creation_date_time')
        read_only_fields = ('id', 'confirmed', 'creation_date_date', 'creation_date_time')


class AlarmOrderSerializer(serializers.ModelSerializer):
    """Default alarm order serializer"""

    rule = AlarmRuleSerializer()

    class Meta:
        model = AlarmOrder
        fields = ('id', 'user', 'grant_privilege', 'creation_date_date', 'creation_date_time', 'rule')
        read_only_fields = ('id', 'creation_date_date', 'creation_date_time')
