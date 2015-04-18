# -*- coding: utf-8 -*-

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

from .models import AlarmZone, AlarmRule
from .apiSerializers import AlarmZoneSerializer


class AlarmZoneViewset(viewsets.ModelViewSet):
    """
    Alarm zone API viewset.

    """
    queryset = AlarmZone.objects.all()
    serializer_class = AlarmZoneSerializer

    @detail_route(methods=['get'])
    def persons_count(self, request, pk):
        # TODO: finish later...
        resp = {}
        zone = self.get_object()
        rules = AlarmRule.objects.filter(zone__id=zone.id)
        resp['count'] = -1
        return Response(resp)
