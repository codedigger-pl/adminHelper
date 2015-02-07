# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ForeignKey, CharField, BooleanField, TextField, DateTimeField


class PersonGroup(models.Model):
    """ Class PersonGroup

    Describes all information about persons groups
    """
    # group name
    name = CharField(max_length=25,
                     unique=True)
    # group description
    description = TextField(blank=True)

    # ---== read only fields ==---
    # group creation date
    creation_date = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Grupa osób'
        verbose_name_plural = 'Grupy osób'

    def __str__(self):
        return self.name


class Person(models.Model):
    """ Class Person

    Describes all information about person in any system
    """
    # person first name
    first_name = CharField(max_length=25)
    # person last name
    last_name = CharField(max_length=25)
    # person is active?
    is_active = BooleanField(default=True)
    # person access system card number
    card_number = CharField(max_length=15)
    # person rank (pan/pani/kpt./mjr/por. etc
    # TODO: change this to CHOICE field after collecting all ranks
    rank = CharField(max_length=25)
    # person group
    group = ForeignKey('PersonGroup')

    # ---== read only fields ==---
    # person creation date
    creation_date = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Osoba'
        verbose_name_plural = 'Osoby'

        unique_together = (('first_name', 'last_name'))

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class SysUser(AbstractUser):
    """ Class SysUser

    Django User class
    """
    pass
