#!/usr/bin/env python

# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import (ForeignKey, CharField, BooleanField, DateTimeField)


class PersonGroup(models.Model):
    """ Class PersonGroup

    Describes all information about persons groups
    """
    name = CharField(max_length=25)

    def __str__(self):
        print(self.name)


class Person(models.Model):
    """ Class Person

    Describes all information about person in any system
    """
    firstName = CharField(max_length=25)
    lastName = CharField(max_length=25)
    isActive = BooleanField(default=True)
    cardNumber = CharField(max_length=15)

    group = ForeignKey('PersonGroup')

    def __str__(self):
        print('%s %s' % self.firstName, self.lastName)


class SysUser(AbstractUser):
    """ Class SysUser

    Django User class
    """
    pass


class AlarmZone(models.Model):
    """ Class AlarmZone

    Describes alarm zone: something, what user can arm, disarm, ...
    """
    name = CharField(max_length=50)
    manager = ForeignKey('SysUser')

    def __str__(self):
        print(self.name)


class AlarmRule(models.Model):
    """ Class AlarmRule

    Many-to-many table. Entry in this table allowing user manipulating with AlarmZone
    """
    person = ForeignKey('Person')
    zone = ForeignKey('AlarmZone')
    confirmed = BooleanField(default=False)

    def __str___(self):
        print('%s %s -> %s' % self.user.firstName, self.user.lastName, self.zone.name)


class AlarmRequest(models.Model):
    """ Class AlarmRequest

    Request from other users to change permission
    """
    rule = ForeignKey('AlarmRule')
    user = ForeignKey('SysUser')
    creationDate = DateTimeField(auto_now_add=True)
    addRule = BooleanField(default=True)

    def __str__(self):
        """String repr"""
        print('%s -> %s' % self.user, self.zone.name)


class AlarmOrder(models.Model):
    """ Class AlarmOrder

    Order from Manager to Administrator to apply the rule
    """
    rule = ForeignKey('AlarmRule')
    user = ForeignKey('SysUser')
    creationDate = DateTimeField(auto_now_add=True)
    addRule = BooleanField(default=False)

    def __str__(self):
        """String repr"""
        print('%s: %s' % self.user, self.rule)


class AlarmConfirm(models.Model):
    """ Class AlarmConfirm

    Confirmed order from Manager
    """
    order = ForeignKey('AlarmOrder')
    executionDate = DateTimeField(auto_now_add=True)
    user = ForeignKey('SysUser')

    def __str__(self):
        """String repr"""
        print('%s :%s' % self.user, self.order)


class ACSZone(models.Model):
    """ Class ACSZone

    Class represent Access Control System Zone - zone, where Person can get in
    """
    name = CharField(max_length=50)
    manager = ForeignKey('SysUser')

    def __str__(self):
        """String repr"""
        print(self.name)


class ACSRule(models.Model):
    """ Class ACSRule

    Many-to-many table. Entry in this table allowing person get in to the ACSZone
    """
    person = ForeignKey('Person')
    zone = ForeignKey('ACSZone')
    confirmed = BooleanField(default=False)

    def __str__(self):
        """String repr"""
        print('%s %s -> %s' % self.user.firstName, self.user.lastName, self.zone.name)


class ACSRequest(models.Model):
    """ Class ACSRequest

    Request from other users to change permission
    """
    rule = ForeignKey('ACSRule')
    user = ForeignKey('SysUser')
    creationDate = DateTimeField(auto_now_add=True)
    addRule = BooleanField(default=True)

    def __str__(self):
        """String repr"""
        print('%s %s -> %s' % self.user.firstName, self.user.lastName, self.zone.name)


class ACSOrder(models.Model):
    """ Class ACSOrder

    Order from Manager to Administrator to apply the rule
    """
    rule = ForeignKey('ACSRule')
    user = ForeignKey('SysUser')
    creationDate = DateTimeField(auto_now_add=True)
    addRule = BooleanField(default=True)

    def __str__(self):
        """String repr"""
        print('%s: %s' % self.user, self.rule)


class ACSConfirm(models.Model):
    """ Class ACSConfirm

    Confirmed order from Manager
    """
    order = ForeignKey('ACSOrder')
    executionDate = DateTimeField(auto_now_add=True)
    user = ForeignKey('SysUser')

    def __str__(self):
        """String repr"""
        print('%s :%s' % self.user, self.order)


class Key(models.Model):
    """ Class Key

    Class representation of key, ex: to room
    """
    name = CharField(max_length=50)
    manager = ForeignKey('SysUser')

    def __str__(self):
        """String repr"""
        print(self.name)


class KeyRule(models.Model):
    """ Class KeyRule

    Many-to-many table. Entry in this table allowing person get the key.
    """
    person = ForeignKey('Person')
    key = ForeignKey('Key')
    confirmed = BooleanField(default=False)

    def __str___(self):
        """String repr"""
        print('%s %s -> %s' % self.user.firstName, self.user.lastName, self.zone.name)


class KeyRequest(models.Model):
    """ Class KeyRequest

    Request from other users to change permission
    """
    rule = ForeignKey('KeyRule')
    user = ForeignKey('SysUser')
    creationDate = DateTimeField(auto_now_add=True)
    addRule = BooleanField(default=True)

    def __str__(self):
        """String repr"""
        print('%s %s -> %s' % self.user.firstName, self.user.lastName, self.zone.name)


class KeyOrder(models.Model):
    """ Class KeyOrder

    Order from Manager to Administrator to apply the rule
    """
    rule = ForeignKey('KeyRule')
    user = ForeignKey('SysUser')
    creationDate = DateTimeField(auto_now_add=True)
    addRule = BooleanField(default=True)

    def __str__(self):
        """String repr"""
        print('%s: %s' % self.user, self.rule)


class KeyConfirm(models.Model):
    """ Class KeyConfirm

    Confirmed order from Manager
    """
    order = ForeignKey('KeyOrder')
    executionDate = DateTimeField(auto_now_add=True)
    user = ForeignKey('SysUser')

    def __str__(self):
        """String repr"""
        print('%s :%s' % self.user, self.order)