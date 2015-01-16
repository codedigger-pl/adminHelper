#!/usr/bin/env python

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db.models import (ForeignKey, IntegerField, CharField, BooleanField,
                              DateTimeField)

#------------------------------------------------------------------------------
# all User classes
#
class Group(models.Model):
    name = CharField(max_length=25)

class User(models.Model):
    firstName = CharField(max_length=25)
    lastName = CharField(max_length=25)
    isActive = BooleanField()
    cardNumber = IntegerField()

    group = ForeignKey('Group')

#------------------------------------------------------------------------------
# Django system User
class SysUser(AbstractBaseUser):
    pass

#------------------------------------------------------------------------------
# all alarm classes
class AlarmZone(models.Model):
    name = CharField(max_length=50)
    manager = ForeignKey('SysUser')

class AlarmRule(models.Model):
    user = ForeignKey('User')
    zone = ForeignKey('AlarmZone')

class AlarmRequest(models.Model):
    rule = ForeignKey('AlarmRule')
    user = ForeignKey('SysUser')

class AlarmOrder(models.Model):
    rule = ForeignKey('AlarmRule')
    user = ForeignKey('SysUser')
    creationDate = DateTimeField()

class AlarmAction(models.Model):
    order = ForeignKey('AlarmOrder')
    executionDate = DateTimeField()
    user = ForeignKey('SysUSer')