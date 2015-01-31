from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from rest_framework import viewsets
from rest_framework.response import Response

from .models import PersonGroup, Person, SysUser
from .apiSerializers import DefPersonGroupSerializer, PersonSerializer, MinimalPersonSerializer


class UserHomepage(TemplateView):
    template_name = 'base.html'


class PersonsList(ListView):
    model = Person
    template_name = 'personsList.html'


def UsersOverview(request):
    resp = {}
    resp['personsCount'] = Person.objects.count()

    lastRegisteredPerson = Person.objects.last()
    if lastRegisteredPerson is not None:
        resp['lastRegisteredPerson'] = lastRegisteredPerson.last_name + ' ' + lastRegisteredPerson.first_name

    return render(request, 'usersOverview.html', resp)


class PersonGroupViewset(viewsets.ModelViewSet):
    queryset = PersonGroup.objects.all()
    serializer_class = DefPersonGroupSerializer


class PersonViewset(viewsets.ModelViewSet):
    """Person viewset

    Defines API all methods to Person"""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def list(self, request, *args, **kwargs):
        queryset = Person.objects.all()

        if 'modelType' in request.QUERY_PARAMS:
            if request.QUERY_PARAMS['modelType'] == 'minimal':
                self.serializer_class = MinimalPersonSerializer

        if 'onlyLastItems' in request.QUERY_PARAMS:
            lastItems = int(request.QUERY_PARAMS['onlyLastItems'])
            startIndex = 0 if queryset.count() - lastItems < 0 else queryset.count() - lastItems
            queryset = queryset[startIndex:]

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
