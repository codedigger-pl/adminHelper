#!/usr/bin/env python

# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ForeignKey, CharField, BooleanField


class PersonGroup(models.Model):
    """ Class PersonGroup

    Describes all information about persons groups
    """
    name = CharField(max_length=25)

    class Meta:
        verbose_name = 'Grupa osób'
        verbose_name_plural = 'Grupy osób'

    def __str__(self):
        return self.name


class Person(models.Model):
    """ Class Person

    Describes all information about person in any system
    """
    firstName = CharField(max_length=25)
    lastName = CharField(max_length=25)
    isActive = BooleanField(default=True)
    cardNumber = CharField(max_length=15)

    group = ForeignKey('PersonGroup')

    class Meta:
        verbose_name = 'Osoba'
        verbose_name_plural = 'Osoby'

    def __str__(self):
        return '%s %s' % (self.firstName, self.lastName)


class SysUser(AbstractUser):
    """ Class SysUser

    Django User class
    """
    pass
