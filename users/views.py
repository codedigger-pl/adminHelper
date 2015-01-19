from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework import viewsets

from .models import PersonGroup, Person, SysUser
from .apiSerializers import DefPersonGroupSerializer, PersonSerializer

class UserHomepage(TemplateView):
    template_name = 'users.html'

class PersonGroupViewset(viewsets.ModelViewSet):
    queryset = PersonGroup.objects.all()
    serializer_class = DefPersonGroupSerializer

class PersonViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer