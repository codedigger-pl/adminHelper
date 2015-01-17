#!/usr/bin/env python

# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import ForeignKey, CharField, BooleanField, DateTimeField

from users.models import Person, SysUser

class ACSZone(models.Model):
    """ Class ACSZone

    Class represent Access Control System Zone - zone, where Person can get in
    """
    name = CharField(max_length=50)
    manager = ForeignKey(SysUser)

    class Meta:
        verbose_name = 'Strefa systemu KD'
        verbose_name_plural = 'Strefy systemu'

    def __str__(self):
        """String repr"""
        return self.name


class ACSRule(models.Model):
    """ Class ACSRule

    Many-to-many table. Entry in this table allowing person get in to the ACSZone
    """
    person = ForeignKey(Person)
    zone = ForeignKey(ACSZone)
    confirmed = BooleanField(default=False)

    class Meta:
        verbose_name = 'Uprawnienie'
        verbose_name_plural = 'Uprawnienia'

    def __str__(self):
        """String repr"""
        return '%s %s -> %s' % (self.person.firstName, self.person.lastName, self.zone.name)


class ACSRequest(models.Model):
    """ Class ACSRequest

    Request from other users to change permission
    """
    rule = ForeignKey(ACSRule)
    user = ForeignKey(SysUser)
    creationDate = DateTimeField(auto_now_add=True)
    addRule = BooleanField(default=True)

    class Meta:
        verbose_name = 'Prośba zmiany uprawnień'
        verbose_name_plural = 'Prośby zmiany uprawnień'

    def __str__(self):
        """String repr"""
        return '%s %s -> %s' % (self.user.first_name, self.user.last_name, self.rule.zone.name)


class ACSOrder(models.Model):
    """ Class ACSOrder

    Order from Manager to Administrator to apply the rule
    """
    rule = ForeignKey(ACSRule)
    user = ForeignKey(SysUser)
    creationDate = DateTimeField(auto_now_add=True)
    addRule = BooleanField(default=True)

    class Meta:
        verbose_name = 'Polecenie zmiany uprawnień'
        verbose_name_plural = 'Polecenia zmiany uprawnień'

    def __str__(self):
        """String repr"""
        return '%s: %s' % (self.user, self.rule)


class ACSConfirm(models.Model):
    """ Class ACSConfirm

    Confirmed order from Manager
    """
    order = ForeignKey(ACSOrder)
    executionDate = DateTimeField(auto_now_add=True)
    user = ForeignKey(SysUser)

    class Meta:
        verbose_name = 'Potwierdzenie zmiany uprawnień'
        verbose_name_plural = 'Potwierdzenia zmiany uprawnień'

    def __str__(self):
        """String repr"""
        return '%s :%s' % (self.user, self.order)