# -*- coding: utf-8 -*-

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

from .models import AlarmZone
from .apiSerializers import AlarmZoneSerializer


class AlarmZoneViewset(viewsets.ModelViewSet):
    """
    Alarm zone API viewset.

    """
    queryset = AlarmZone.objects.all()
    serializer_class = AlarmZoneSerializer
