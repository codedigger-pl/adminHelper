#!/usr/bin/env python

# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import ForeignKey, CharField, BooleanField, DateTimeField

from users.models import Person, SysUser


class Key(models.Model):
    """ Class Key

    Class representation of key, ex: to room
    """
    name = CharField(max_length=50)
    manager = ForeignKey(SysUser)

    class Meta:
        verbose_name = 'Klucz'
        verbose_name_plural = 'Klucze'

    def __str__(self):
        """String repr"""
        return self.name


class KeyRule(models.Model):
    """ Class KeyRule

    Many-to-many table. Entry in this table allowing person get the key.
    """
    person = ForeignKey(Person)
    key = ForeignKey(Key)
    confirmed = BooleanField(default=False)

    class Meta:
        verbose_name = 'Uprawnienie'
        verbose_name_plural = 'Uprawnienia'

    def __str__(self):
        """String repr"""
        return '%s %s -> %s' % (self.person.firstName, self.person.lastName, self.key.name)


class KeyRequest(models.Model):
    """ Class KeyRequest

    Request from other users to change permission
    """
    rule = ForeignKey(KeyRule)
    user = ForeignKey(SysUser)
    creationDate = DateTimeField(auto_now_add=True)
    addRule = BooleanField(default=True)

    class Meta:
        verbose_name = 'Prośba zmiany uprawnień'
        verbose_name_plural = 'Prośby zmiany uprawnień'

    def __str__(self):
        """String repr"""
        return '%s %s -> %s' % (self.user.first_name, self.user.last_name, self.rule.key.name)


class KeyOrder(models.Model):
    """ Class KeyOrder

    Order from Manager to Administrator to apply the rule
    """
    rule = ForeignKey(KeyRule)
    user = ForeignKey(SysUser)
    creationDate = DateTimeField(auto_now_add=True)
    addRule = BooleanField(default=True)

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