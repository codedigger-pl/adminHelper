# -*- coding: utf-8 -*-

from rest_framework import serializers

from users.apiSerializers import DefUserSerializer
from .models import AlarmZone


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