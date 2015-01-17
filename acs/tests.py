#!/usr/bin/env python

# -*- coding: utf-8 -*-


from django.test import TestCase

from users.models import SysUser, Person, PersonGroup

from .models import ACSConfirm, ACSRequest, ACSOrder, ACSRule, ACSZone

# some basic class creators
def create_SysUser1(): return SysUser.objects.create_user(username='Manager 1')

def create_PersonGroup1(): return PersonGroup.objects.create(name='Group 1')
def create_Person1(): return Person.objects.create(firstName='First name',
                                                   lastName='Last name',
                                                   isActive=True,
                                                   cardNumber='123',
                                                   group=create_PersonGroup1())

def create_ACSZone1(): return ACSZone.objects.create(name='Zone 1', manager=create_SysUser1())
def create_ACSRule1(): return ACSRule.objects.create(person=create_Person1(), zone=create_ACSZone1())
def create_ACSOrder(): return ACSOrder.objects.create(rule=create_ACSRule1(),
                                                      user=SysUser.objects.create_user(username='Manager 2'))


class ACSZoneTest(TestCase):
    def setUp(self):
        manager = create_SysUser1()
        ACSZone.objects.create(name='Zone 1', manager=manager)
        ACSZone.objects.create(name='Zone 2', manager=manager)

    def test_basic(self):
        zone1 = ACSZone.objects.get(name='Zone 1')
        zone2 = ACSZone.objects.get(name='Zone 2')
        manager = SysUser.objects.get(id=1)

        self.assertEqual(zone1.name, 'Zone 1')
        self.assertEqual(zone2.name, 'Zone 2')

        self.assertEqual(zone1.manager, manager)
        self.assertEqual(zone2.manager, manager)

    def test_str(self):
        zone = ACSZone.objects.get(name='Zone 1')
        self.assertNotEqual(str(zone), '')


class ACSRuleTest(TestCase):
    def setUp(self):
        create_Person1()
        create_ACSZone1()

    def test_basic(self):
        person = Person.objects.get(id=1)
        zone = ACSZone.objects.get(id=1)

        rule1 = ACSRule.objects.create(person=person, zone=zone)
        rule2 = ACSRule.objects.create(person=person, zone=zone, confirmed=True)

        self.assertEqual(rule1.zone, zone)
        self.assertEqual(rule1.person, person)
        self.assertEqual(rule1.confirmed, False)

        self.assertEqual(rule2.confirmed, True)

    def test_str(self):
        person = Person.objects.get(id=1)
        zone = ACSZone.objects.get(id=1)

        obj = ACSRule.objects.create(person=person, zone=zone)
        self.assertNotEqual(str(obj), '')


class ACSRequestTest(TestCase):
    def setUp(self):
        create_ACSRule1()

    def test_basic(self):
        #TODO: Add date checking after changing it
        rule = ACSRule.objects.get(id=1)
        user = rule.zone.manager

        req1 = ACSRequest.objects.create(user=user, rule=rule)
        req2 = ACSRequest.objects.create(user=user, rule=rule, addRule=False)

        self.assertEqual(req1.user, user)
        self.assertEqual(req1.rule, rule)
        self.assertEqual(req1.addRule, True)
        self.assertIsNotNone(req1.creationDate)

        self.assertEqual(req2.addRule, False)

    def test_str(self):
        rule = ACSRule.objects.get(id=1)
        user = rule.zone.manager

        obj = ACSRequest.objects.create(user=user, rule=rule)
        self.assertNotEqual(str(obj), '')


class ACSOrdertTest(TestCase):
    def setUp(self):
        create_ACSRule1()

    def test_basic(self):
        #TODO: Add date checking after changing it
        rule = ACSRule.objects.get(id=1)
        user = rule.zone.manager

        order1 = ACSRequest.objects.create(user=user, rule=rule)
        order2 = ACSRequest.objects.create(user=user, rule=rule, addRule=False)

        self.assertEqual(order1.user, user)
        self.assertEqual(order1.rule, rule)
        self.assertEqual(order1.addRule, True)
        self.assertIsNotNone(order1.creationDate)

        self.assertEqual(order2.addRule, False)

    def test_str(self):
        rule = ACSRule.objects.get(id=1)
        user = rule.zone.manager

        obj = ACSRequest.objects.create(user=user, rule=rule)
        self.assertNotEqual(str(obj), '')


class ACSConfirmtTest(TestCase):
    def setUp(self):
        create_ACSOrder()

    def test_basic(self):
        order = ACSOrder.objects.get(id=1)
        user = SysUser.objects.get(id=2)

        confirm = ACSConfirm.objects.create(order=order, user=user)

        self.assertEqual(confirm.user, user)
        self.assertEqual(confirm.order, order)
        self.assertIsNotNone(confirm.executionDate)

    def test_str(self):
        order = ACSOrder.objects.get(id=1)
        user = SysUser.objects.get(id=2)

        obj = ACSConfirm.objects.create(order=order, user=user)
        self.assertNotEqual(str(obj), '')