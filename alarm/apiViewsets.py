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
        resp = {}
        zone = self.get_object()
        resp['count'] = zone.persons.count()
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

        if 'nonExecutedOnly' in request.QUERY_PARAMS:
            self.queryset = AlarmOrder.objects.filter(executed=False)

        return super(AlarmOrderViewset, self).list(request, args, kwargs)

    @detail_route(methods=['post'])
    def execute(self, request, pk):
        order = self.get_object()
        order.executed = True
        order.save()
        person = order.rule.person
        zone = order.rule.zone
        if order.grant_privilege:
            zone.persons.add(person)
        else:
            zone.persons.remove(person)
        zone.save()
        return Response({'result': 'user added to zone'}, status=status.HTTP_200_OK)


class AlarmRequestViewset(viewsets.ModelViewSet):
    """Alarm request API viewset"""

    queryset = AlarmRequest.objects.all()
    serializer_class = AlarmRequestSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = ListAlarmRequestSerializer
        return super(AlarmRequestViewset, self).list(request, args, kwargs)