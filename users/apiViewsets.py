# -*- coding: utf-8 -*-

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

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


class PersonViewset(viewsets.ModelViewSet):
    """Person viewset

    Defines API all methods to Person"""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_class = PersonFilter

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
