# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import AlarmZone


class AlarmZoneSerializer(serializers.ModelSerializer):
    """
    Default person group serializer.
    """
    class Meta:
        model = AlarmZone
        fields = ('id', 'name', 'description', 'creation_date_date', 'creation_date_time', 'manager')
        read_only_fields = ('id', 'creation_date_date', 'creation_date_time')
