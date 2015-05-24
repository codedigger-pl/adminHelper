# -*- coding: utf-8 -*-

from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

from .models import Key, KeyRule, KeyOrder, KeyRequest

from .apiSerializers import KeySerializer, ListKeySerializer
from .apiSerializers import KeyRuleSerializer, ListKeyOrderSerializer, KeyOrderSerializer
from .apiSerializers import KeyRequestSerializer, ListKeyRequestSerializer


class KeyViewset(viewsets.ModelViewSet):
    """Key key API viewset"""

    queryset = Key.objects.all()
    serializer_class = KeySerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = ListKeySerializer
        return super(KeyViewset, self).list(request, args, kwargs)

    @detail_route(methods=['get'])
    def persons_count(self, request, pk):
        resp = {}
        key = self.get_object()
        resp['count'] = key.persons.count()
        return Response(resp)


class KeyRuleViewset(viewsets.ModelViewSet):
    """Key rule API viewset"""

    queryset = KeyRule.objects.all()
    serializer_class = KeyRuleSerializer


class KeyOrderViewset(viewsets.ModelViewSet):
    """Key order API viewset"""

    queryset = KeyOrder.objects.all()
    serializer_class = KeyOrderSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = ListKeyOrderSerializer

        if 'nonExecutedOnly' in request.QUERY_PARAMS:
            self.queryset = KeyOrder.objects.filter(executed=False)

        return super(KeyOrderViewset, self).list(request, args, kwargs)

    @detail_route(methods=['post'])
    def execute(self, request, pk):
        order = self.get_object()
        order.executed = True
        order.save()
        person = order.rule.person
        key = order.rule.key
        if order.grant_privilege:
            key.persons.add(person)
        else:
            key.persons.remove(person)
        key.save()
        return Response({'result': 'user added to key'}, status=status.HTTP_200_OK)


class KeyRequestViewset(viewsets.ModelViewSet):
    """Key request API viewset"""

    queryset = KeyRequest.objects.all()
    serializer_class = KeyRequestSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = ListKeyRequestSerializer
        return super(KeyRequestViewset, self).list(request, args, kwargs)