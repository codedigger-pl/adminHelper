# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAuthenticated

from alarm.models import AlarmZone
from acs.models import ACSZone
from key.models import Key

from .models import PersonGroup, Person, SysUser

from .filters import PersonFilter

from .apiSerializers import DefPersonGroupSerializer, PersonSerializer, MinimalPersonSerializer
from .apiSerializers import DefUserSerializer, UserPasswordSerializer


class PersonGroupViewset(viewsets.ModelViewSet):
    """
    Person API viewset.

    """
    queryset = PersonGroup.objects.all()
    serializer_class = DefPersonGroupSerializer
    permission_classes = (IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        """
        Return person groups list based on params.

        :param request: request
        :param args: not used
        :param kwargs: dictionary can be:
            onlyLastItems: {int} - how many last items return
        :return: list of person groups based on params
        """

        queryset = PersonGroup.objects.all()

        if 'onlyLastItems' in request.QUERY_PARAMS:
            lastItems = int(request.QUERY_PARAMS['onlyLastItems'])
            startIndex = 0 if queryset.count() - lastItems < 0 else queryset.count() - lastItems
            queryset = queryset[startIndex:]

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def count(self, request):
        resp = {}
        resp['count'] = PersonGroup.objects.count()
        return Response(resp, status=status.HTTP_200_OK)

    @list_route(methods=['get'])
    def last_registered(self, request):
        resp = {}
        resp['name'] = PersonGroup.objects.last().name
        return Response(resp, status=status.HTTP_200_OK)

    @detail_route(methods=['get'])
    def person_count(self, request, pk):
        group = self.get_object()
        resp = {}
        resp['count'] = group.person_set.count()
        return Response(resp)


class PersonViewset(viewsets.ModelViewSet):
    """Person viewset

    Defines API all methods to Person"""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_class = PersonFilter
    permission_classes = (IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        """
        Return person list based on params.
        :param request: request
        :param args: not used
        :param kwargs: dictionary can be:
            modelType: 'minimal' - return minimal information about persons
            onlyLastItems: {int} - how many last items return
        :return: list of persons based on params
        """

        queryset = self.filter_queryset(self.get_queryset())

        if 'modelType' in request.QUERY_PARAMS:
            if request.QUERY_PARAMS['modelType'] == 'minimal':
                self.serializer_class = MinimalPersonSerializer

        if 'onlyLastItems' in request.QUERY_PARAMS:
            lastItems = int(request.QUERY_PARAMS['onlyLastItems'])
            startIndex = 0 if queryset.count() - lastItems < 0 else queryset.count() - lastItems
            queryset = queryset[startIndex:]

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     print(request.data)

    @list_route(methods=['get'])
    def count(self, request):
        resp = {}
        resp['count'] = Person.objects.count()
        return Response(resp, status=status.HTTP_200_OK)

    @list_route(methods=['get'])
    def last_registered(self, request):
        last_person = Person.objects.last()
        resp = {}
        resp['name'] = last_person.last_name + ' ' + last_person.first_name
        return Response(resp, status=status.HTTP_200_OK)

    @detail_route(methods=['get'])
    def alarm_zones(self, request, pk):
        person = self.get_object()
        user_zones = AlarmZone.objects.filter(persons=person)
        zones = AlarmZone.objects.all()
        resp = []
        for zone in zones:
            resp.append({'id': zone.id,
                         'name': zone.name,
                         'has_access': zone in user_zones})
        return Response(resp, status=status.HTTP_200_OK)

    @detail_route(methods=['get'])
    def acs_zones(self, request, pk):
        person = self.get_object()
        user_zones = ACSZone.objects.filter(persons=person)
        zones = ACSZone.objects.all()
        resp = []
        for zone in zones:
            resp.append({'id': zone.id,
                         'name': zone.name,
                         'has_access': zone in user_zones})
        return Response(resp, status=status.HTTP_200_OK)

    @detail_route(methods=['get'])
    def keys(self, request, pk):
        person = self.get_object()
        user_keys = Key.objects.filter(persons=person)
        keys = Key.objects.all()
        resp = []
        for key in keys:
            resp.append({'id': key.id,
                         'name': key.name,
                         'has_access': key in user_keys})
        return Response(resp, status=status.HTTP_200_OK)


class UserViewset(viewsets.ModelViewSet):
    """User viewset

    Defines API all methods to User"""
    queryset = SysUser.objects.all()
    serializer_class = DefUserSerializer

    @detail_route(methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = UserPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'hasło zmienione'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['get'])
    def count(self, request):
        resp = {}
        resp['count'] = SysUser.objects.count()
        return Response(resp, status=status.HTTP_200_OK)

    @list_route(methods=['get'])
    def last_registered(self, request):
        last_user = SysUser.objects.last()
        resp = {}
        resp['name'] = last_user.last_name + ' ' + last_user.first_name
        return Response(resp, status=status.HTTP_200_OK)

    @list_route(methods=['post'])
    def login(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            resp = {}
            resp['id'] = user.id
            login(request, user)
            return Response(resp, status=status.HTTP_200_OK)

        return Response({}, status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['get'])
    def logged_user(self, request):
        if request.user.is_anonymous():
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            resp = {}
            resp['id'] = request.user.id
            return Response(resp, status=status.HTTP_200_OK)
