#!/usr/bin/env python

# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import ForeignKey, CharField, BooleanField, DateTimeField, TextField

from users.models import SysUser, Person


class AlarmZone(models.Model):
    """ Class AlarmZone

    Describes alarm zone: something, what user can arm, disarm, ...
    """
    name = CharField(max_length=50)
    description = TextField(blank=True)
    manager = ForeignKey(SysUser)

    # ---== read only fields ==---
    # zone creation date
    creation_date = DateTimeField(auto_now_add=True)
    creation_date_date = property(lambda self: self.creation_date.date())
    creation_date_time = property(lambda self: self.creation_date.time())

    class Meta:
        verbose_name = 'Strefa systemu alarmowego'
        verbose_name_plural = 'Strefy systemu'

    def __str__(self):
        return self.name


class AlarmRule(models.Model):
    """ Class AlarmRule

    Many-to-many table. Entry in this table allowing user manipulating with AlarmZone
    """
    person = ForeignKey(Person)
    zone = ForeignKey(AlarmZone)
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


class AlarmRequest(models.Model):
    """ Class AlarmRequest

    Request from other users to change permission
    """
    rule = ForeignKey(AlarmRule)
    user = ForeignKey(SysUser)
    creationDate = DateTimeField(auto_now_add=True)
    addRule = BooleanField(default=True)

    class Meta:
        verbose_name = 'Prośba zmiany uprawnień'
        verbose_name_plural = 'Prośby zmiany uprawnień'

    def __str__(self):
        """String repr"""
        return '%s -> %s' % (self.user, self.rule.zone.name)


class AlarmOrder(models.Model):
    """ Class AlarmOrder

    Order from Manager to Administrator to apply the rule
    """
    rule = ForeignKey(AlarmRule)
    user = ForeignKey(SysUser)
    grant_privilege = BooleanField(default=False)

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


class AlarmConfirm(models.Model):
    """ Class AlarmConfirm

    Confirmed order from Manager
    """
    order = ForeignKey(AlarmOrder)
    executionDate = DateTimeField(auto_now_add=True)
    user = ForeignKey(SysUser)

    class Meta:
        verbose_name = 'Potwierdzenie zmiany uprawnień'
        verbose_name_plural = 'Potwierdzenia zmiany uprawnień'

    def __str__(self):
        """String repr"""
        return '%s :%s' % (self.user, self.order)
