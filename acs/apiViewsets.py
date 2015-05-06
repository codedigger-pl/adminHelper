# -*- coding: utf-8 -*-

from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

from .models import ACSZone, ACSRule, ACSOrder, ACSRequest

from .apiSerializers import ACSZoneSerializer, ListACSZoneSerializer
from .apiSerializers import ACSRuleSerializer, ListACSOrderSerializer, ACSOrderSerializer
from .apiSerializers import ACSRequestSerializer, ListACSRequestSerializer


class ACSZoneViewset(viewsets.ModelViewSet):
    """ACS zone API viewset"""

    queryset = ACSZone.objects.all()
    serializer_class = ACSZoneSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = ListACSZoneSerializer
        return super(ACSZoneViewset, self).list(request, args, kwargs)

    @detail_route(methods=['get'])
    def persons_count(self, request, pk):
        resp = {}
        zone = self.get_object()
        resp['count'] = zone.persons.count()
        return Response(resp)


class ACSRuleViewset(viewsets.ModelViewSet):
    """ACS rule API viewset"""

    queryset = ACSRule.objects.all()
    serializer_class = ACSRuleSerializer


class ACSOrderViewset(viewsets.ModelViewSet):
    """ACS order API viewset"""

    queryset = ACSOrder.objects.all()
    serializer_class = ACSOrderSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = ListACSOrderSerializer

        if 'nonExecutedOnly' in request.QUERY_PARAMS:
            self.queryset = ACSOrder.objects.filter(executed=False)

        return super(ACSOrderViewset, self).list(request, args, kwargs)

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


class ACSRequestViewset(viewsets.ModelViewSet):
    """ACS request API viewset"""

    queryset = ACSRequest.objects.all()
    serializer_class = ACSRequestSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = ListACSRequestSerializer
        return super(ACSRequestViewset, self).list(request, args, kwargs)