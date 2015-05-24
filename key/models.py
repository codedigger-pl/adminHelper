#!/usr/bin/env python

# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import ForeignKey, CharField, BooleanField, DateTimeField, TextField, ManyToManyField

from users.models import SysUser, Person


class Key(models.Model):
    """ Class KeyZone

    Describes Key zone: somewhere, where user can get in or out, ...
    """
    name = CharField(max_length=50)
    description = TextField(blank=True)
    manager = ForeignKey(SysUser)
    persons = ManyToManyField(Person)

    # ---== read only fields ==---
    # zone creation date
    creation_date = DateTimeField(auto_now_add=True)
    creation_date_date = property(lambda self: self.creation_date.date())
    creation_date_time = property(lambda self: self.creation_date.time())

    @property
    def persons_count(self):
        return self.persons.count()

    class Meta:
        verbose_name = 'Strefa systemu Keyowego'
        verbose_name_plural = 'Strefy systemu'

    def __str__(self):
        return self.name


class KeyRule(models.Model):
    """ Class KeyRule

    Many-to-many table. Entry in this table allowing user manipulating with KeyZone
    """
    person = ForeignKey(Person)
    key = ForeignKey(Key)
    confirmed = BooleanField(default=False)

    # ---== read only fields ==---
    # zone creation date
    creation_date = DateTimeField(auto_now_add=True)
    creation_date_date = property(lambda self: self.creation_date.date())
    creation_date_time = property(lambda self: self.creation_date.time())

    class Meta:
        verbose_name = 'Uprawnienie'
        verbose_name_plural = 'Uprawnienia'

    def __str___(self):
        return '%s %s -> %s' % (self.user.firstName, self.user.lastName, self.zone.name)


class KeyRequest(models.Model):
    """ Class KeyRequest

    Request from other users to change permission
    """
    rule = ForeignKey(KeyRule)
    user = ForeignKey(SysUser)
    creationDate = DateTimeField(auto_now_add=True)
    grant_privilege = BooleanField(default=True)

    # ---== read only fields ==---
    # zone creation date
    creation_date = DateTimeField(auto_now_add=True)
    creation_date_date = property(lambda self: self.creation_date.date())
    creation_date_time = property(lambda self: self.creation_date.time())

    class Meta:
        verbose_name = 'Prośba zmiany uprawnień'
        verbose_name_plural = 'Prośby zmiany uprawnień'

    def __str__(self):
        """String repr"""
        return '%s -> %s' % (self.user, self.rule.zone.name)


class KeyOrder(models.Model):
    """ Class KeyOrder

    Order from Manager to Administrator to apply the rule
    """
    rule = ForeignKey(KeyRule)
    user = ForeignKey(SysUser)
    grant_privilege = BooleanField(default=False)
    executed = BooleanField(default=False)

    # ---== read only fields ==---
    # zone creation date
    creation_date = DateTimeField(auto_now_add=True)
    creation_date_date = property(lambda self: self.creation_date.date())
    creation_date_time = property(lambda self: self.creation_date.time())

    class Meta:
        verbose_name = 'Polecenie zmiany uprawnień'
        verbose_name_plural = 'Polecenia zmiany uprawnień'

    def __str__(self):
        """String repr"""
        return '%s: %s' % (self.user, self.rule)


class KeyConfirm(models.Model):
    """ Class KeyConfirm

    Confirmed order from Manager
    """
    order = ForeignKey(KeyOrder)
    executionDate = DateTimeField(auto_now_add=True)
    user = ForeignKey(SysUser)

    class Meta:
        verbose_name = 'Potwierdzenie zmiany uprawnień'
        verbose_name_plural = 'Potwierdzenia zmiany uprawnień'

    def __str__(self):
        """String repr"""
        return '%s :%s' % (self.user, self.order)
