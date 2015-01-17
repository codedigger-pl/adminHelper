#!/usr/bin/env python

# -*- coding: utf-8 -*-


from django.test import TestCase

from users.models import PersonGroup, Person, SysUser

from .models import AlarmConfirm, AlarmOrder, AlarmRequest, AlarmRule, AlarmZone

# some basic class creators
def create_SysUser1(): return SysUser.objects.create_user(username='Manager 1')

def create_PersonGroup1(): return PersonGroup.objects.create(name='Group 1')
def create_Person1(): return Person.objects.create(firstName='First name',
                                                   lastName='Last name',
                                                   isActive=True,
                                                   cardNumber='123',
                                                   group=create_PersonGroup1())

def create_AlarmZone1(): return AlarmZone.objects.create(name='Zone 1', manager=create_SysUser1())
def create_AlarmRule1(): return AlarmRule.objects.create(person=create_Person1(), zone=create_AlarmZone1())
def create_AlarmOrder(): return AlarmOrder.objects.create(rule=create_AlarmRule1(),
                                                          user=SysUser.objects.create_user(username='Manager 2'))


class AlarmZoneTest(TestCase):
    def setUp(self):
        manager1 = create_SysUser1()
        AlarmZone.objects.create(name='Zone 1', manager=manager1)
        AlarmZone.objects.create(name='Zone 2', manager=manager1)

    def test_basic(self):
        zone1 = AlarmZone.objects.get(name='Zone 1')
        zone2 = AlarmZone.objects.get(name='Zone 2')
        manager1 = SysUser.objects.get(id=1)

        self.assertEqual(zone1.name, 'Zone 1')
        self.assertEqual(zone2.name, 'Zone 2')

        self.assertEqual(zone1.manager, manager1)
        self.assertEqual(zone2.manager, manager1)

    def test_str(self):
        obj = AlarmZone.objects.get(name='Zone 1')
        self.assertNotEqual(str(obj), '')


class AlarmRuleTest(TestCase):
    def setUp(self):
        create_Person1()
        create_AlarmZone1()

    def test_basic(self):
        person = Person.objects.get(id=1)
        zone = AlarmZone.objects.get(id=1)

        rule1 = AlarmRule.objects.create(person=person, zone=zone)
        rule2 = AlarmRule.objects.create(person=person, zone=zone, confirmed=True)

        self.assertEqual(rule1.zone, zone)
        self.assertEqual(rule1.person, person)
        self.assertEqual(rule1.confirmed, False)

        self.assertEqual(rule2.confirmed, True)

    def test_str(self):
        person = Person.objects.get(id=1)
        zone = AlarmZone.objects.get(id=1)

        obj = AlarmRule.objects.create(person=person, zone=zone)
        self.assertNotEqual(str(obj), '')


class AlarmRequestTest(TestCase):
    def setUp(self):
        create_AlarmRule1()

    def test_basic(self):
        #TODO: Add date checking after changing it
        rule = AlarmRule.objects.get(id=1)
        user = rule.zone.manager

        req1 = AlarmRequest.objects.create(user=user, rule=rule)
        req2 = AlarmRequest.objects.create(user=user, rule=rule, addRule=False)

        self.assertEqual(req1.user, user)
        self.assertEqual(req1.rule, rule)
        self.assertEqual(req1.addRule, True)
        self.assertIsNotNone(req1.creationDate)

        self.assertEqual(req2.addRule, False)

    def test_str(self):
        rule = AlarmRule.objects.get(id=1)
        user = rule.zone.manager

        obj = AlarmRequest.objects.create(user=user, rule=rule)
        self.assertNotEqual(str(obj), '')


class AlarmOrdertTest(TestCase):
    def setUp(self):
        create_AlarmRule1()

    def test_basic(self):
        #TODO: Add date checking after changing it
        rule = AlarmRule.objects.get(id=1)
        user = rule.zone.manager

        order1 = AlarmRequest.objects.create(user=user, rule=rule)
        order2 = AlarmRequest.objects.create(user=user, rule=rule, addRule=False)

        self.assertEqual(order1.user, user)
        self.assertEqual(order1.rule, rule)
        self.assertEqual(order1.addRule, True)
        self.assertIsNotNone(order1.creationDate)

        self.assertEqual(order2.addRule, False)

    def test_str(self):
        rule = AlarmRule.objects.get(id=1)
        user = rule.zone.manager

        obj = AlarmRequest.objects.create(user=user, rule=rule)
        self.assertNotEqual(str(obj), '')


class AlarmConfirmtTest(TestCase):
    def setUp(self):
        create_AlarmOrder()

    def test_basic(self):
        order = AlarmOrder.objects.get(id=1)
        user = SysUser.objects.get(id=2)

        confirm = AlarmConfirm.objects.create(order=order, user=user)

        self.assertEqual(confirm.user, user)
        self.assertEqual(confirm.order, order)
        self.assertIsNotNone(confirm.executionDate)

    def test_str(self):
        order = AlarmOrder.objects.get(id=1)
        user = SysUser.objects.get(id=2)

        obj = AlarmConfirm.objects.create(order=order, user=user)
        self.assertNotEqual(str(obj), '')