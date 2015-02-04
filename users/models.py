#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ForeignKey, CharField, BooleanField, TextField


class PersonGroup(models.Model):
    """ Class PersonGroup

    Describes all information about persons groups
    """
    name = CharField(max_length=25, unique=True)
    description = TextField(blank=True)

    class Meta:
        verbose_name = 'Grupa osób'
        verbose_name_plural = 'Grupy osób'

    def __str__(self):
        return self.name


class Person(models.Model):
    """ Class Person

    Describes all information about person in any system
    """
    first_name = CharField(max_length=25)
    last_name = CharField(max_length=25)
    is_active = BooleanField(default=True)
    card_number = CharField(max_length=15)

    group = ForeignKey('PersonGroup')

    class Meta:
        verbose_name = 'Osoba'
        verbose_name_plural = 'Osoby'

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class SysUser(AbstractUser):
    """ Class SysUser

    Django User class
    """
    pass
