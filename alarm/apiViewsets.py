# -*- coding: utf-8 -*-

from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

from .models import AlarmZone, AlarmRule, AlarmOrder, AlarmRequest

from .apiSerializers import AlarmZoneSerializer, ListAlarmZoneSerializer
from .apiSerializers import AlarmRuleSerializer, ListAlarmOrderSerializer, AlarmOrderSerializer
from .apiSerializers import AlarmRequestSerializer, ListAlarmRequestSerializer


class AlarmZoneViewset(viewsets.ModelViewSet):
    """Alarm zone API viewset"""

    queryset = AlarmZone.objects.all()
    serializer_class = AlarmZoneSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = ListAlarmZoneSerializer
        return super(AlarmZoneViewset, self).list(request, args, kwargs)

    @detail_route(methods=['get'])
    def persons_count(self, request, pk):
        # TODO: finish later...
        resp = {}
        zone = self.get_object()
        rules = AlarmRule.objects.filter(zone__id=zone.id)
        resp['count'] = -1
        return Response(resp)


class AlarmRuleViewset(viewsets.ModelViewSet):
    """Alarm rule API viewset"""

    queryset = AlarmRule.objects.all()
    serializer_class = AlarmRuleSerializer


class AlarmOrderViewset(viewsets.ModelViewSet):
    """Alarm order API viewset"""

    queryset = AlarmOrder.objects.all()
    serializer_class = AlarmOrderSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = ListAlarmOrderSerializer
        return super(AlarmOrderViewset, self).list(request, args, kwargs)


class AlarmRequestViewset(viewsets.ModelViewSet):
    """Alarm request API viewset"""

    queryset = AlarmRequest.objects.all()
    serializer_class = AlarmRequestSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = ListAlarmRequestSerializer
        return super(AlarmRequestViewset, self).list(request, args, kwargs)