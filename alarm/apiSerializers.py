# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import AlarmZone, AlarmOrder, AlarmRule, AlarmRequest


class AlarmZoneSerializer(serializers.ModelSerializer):
    """Default alarm zone serializer"""

    class Meta:
        model = AlarmZone
        fields = ('id', 'name', 'description', 'creation_date_date', 'creation_date_time', 'manager')
        read_only_fields = ('id', 'creation_date_date', 'creation_date_time')


class ListAlarmZoneSerializer(serializers.ModelSerializer):
    """Alarm zone serializer used to list zones"""

    manager = serializers.StringRelatedField()
    # TODO: test it after migrate to normal database
    # persons_count = serializers.ReadOnlyField(source="AlarmRule.objects.filter(zone_id=id).distinct('person')")

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

    class Meta:
        model = AlarmOrder
        fields = ('id', 'user', 'grant_privilege', 'creation_date_date', 'creation_date_time', 'rule')
        read_only_fields = ('id', 'creation_date_date', 'creation_date_time')


class ListAlarmOrderSerializer(serializers.ModelSerializer):
    """Alarm order serializer used in lists"""

    rule_zone = serializers.ReadOnlyField(source='rule.zone.name')
    rule_person = serializers.StringRelatedField(source='rule.person')

    class Meta:
        model = AlarmOrder
        fields = ('id', 'user', 'grant_privilege', 'rule_zone', 'rule_person')
        read_only_fields = ('id', )


class AlarmRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlarmRequest
        fields = ('id', 'creation_date_date', 'creation_date_time', 'user', 'rule', 'grant_privilege')
        read_only_fields = ('id', 'creation_date_date', 'creation_date_time')


class ListAlarmRequestSerializer(serializers.ModelSerializer):

    rule_zone = serializers.ReadOnlyField(source='rule.zone.name')
    rule_person = serializers.StringRelatedField(source='rule.person')
    user = serializers.StringRelatedField()

    class Meta:
        model = AlarmRequest
        fields = ('id', 'user', 'rule_zone', 'rule_person', 'grant_privilege')
        read_only_fields = ('id', )
