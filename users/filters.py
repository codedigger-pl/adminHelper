# -*- coding: utf-8 -*-

from django_filters import FilterSet, CharFilter

from .models import Person


class PersonFilter(FilterSet):
    """ Default person filter.
    """
    first_name = CharFilter(lookup_type='icontains', name='first_name')
    last_name = CharFilter(lookup_type='icontains', name='last_name')
    class Meta:
        model = Person
        fields = ('first_name', 'last_name')