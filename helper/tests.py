#!/usr/bin/env python

# -*- coding: utf-8 -*-


from django.test import TestCase

from .models import (ACSConfirm, ACSRequest, ACSOrder, ACSRule, ACSZone,
                     AlarmConfirm, AlarmOrder, AlarmRequest, AlarmRule, AlarmZone,
                     Key, KeyConfirm, KeyOrder, KeyRequest, KeyRule,
                     Person, PersonGroup, SysUser)

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

def create_AlarmZone1(): return AlarmZone.objects.create(name='Zone 1', manager=create_SysUser1())
def create_AlarmRule1(): return AlarmRule.objects.create(person=create_Person1(), zone=create_AlarmZone1())
def create_AlarmOrder(): return AlarmOrder.objects.create(rule=create_AlarmRule1(),
                                                          user=SysUser.objects.create_user(username='Manager 2'))

def create_Key1(): return Key.objects.create(name='Key 1', manager=create_SysUser1())
def create_KeyRule1(): return KeyRule.objects.create(person=create_Person1(), key=create_Key1())
def create_KeyOrder(): return KeyOrder.objects.create(rule=create_KeyRule1(),
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


class KeyTest(TestCase):
    def setUp(self):
        manager1 = create_SysUser1()
        Key.objects.create(name='Key 1', manager=manager1)
        Key.objects.create(name='Key 2', manager=manager1)

    def test_basic(self):
        key1 = Key.objects.get(name='Key 1')
        key2 = Key.objects.get(name='Key 2')
        manager1 = SysUser.objects.get(id=1)

        self.assertEqual(key1.name, 'Key 1')
        self.assertEqual(key2.name, 'Key 2')

        self.assertEqual(key1.manager, manager1)
        self.assertEqual(key2.manager, manager1)

    def test_str(self):
        obj =  Key.objects.get(name='Key 1')
        self.assertNotEqual(str(obj), '')


class KeyRuleTest(TestCase):
    def setUp(self):
        create_Person1()
        create_Key1()

    def test_basic(self):
        person = Person.objects.get(id=1)
        key = Key.objects.get(id=1)

        rule1 = KeyRule.objects.create(person=person, key=key)
        rule2 = KeyRule.objects.create(person=person, key=key, confirmed=True)

        self.assertEqual(rule1.key, key)
        self.assertEqual(rule1.person, person)
        self.assertEqual(rule1.confirmed, False)

        self.assertEqual(rule2.confirmed, True)

    def test_str(self):
        person = Person.objects.get(id=1)
        key = Key.objects.get(id=1)

        obj = KeyRule.objects.create(person=person, key=key)
        self.assertNotEqual(str(obj), '')


class KeyRequestTest(TestCase):
    def setUp(self):
        create_KeyRule1()

    def test_basic(self):
        #TODO: Add date checking after changing it
        rule = KeyRule.objects.get(id=1)
        user = rule.key.manager

        req1 = KeyRequest.objects.create(user=user, rule=rule)
        req2 = KeyRequest.objects.create(user=user, rule=rule, addRule=False)

        self.assertEqual(req1.user, user)
        self.assertEqual(req1.rule, rule)
        self.assertEqual(req1.addRule, True)
        self.assertIsNotNone(req1.creationDate)

        self.assertEqual(req2.addRule, False)

    def test_str(self):
        rule = KeyRule.objects.get(id=1)
        user = rule.key.manager

        obj = KeyRequest.objects.create(user=user, rule=rule)
        self.assertNotEqual(str(obj), '')


class KeyOrdertTest(TestCase):
    def setUp(self):
        create_KeyRule1()

    def test_basic(self):
        #TODO: Add date checking after changing it
        rule = KeyRule.objects.get(id=1)
        user = rule.key.manager

        order1 = KeyRequest.objects.create(user=user, rule=rule)
        order2 = KeyRequest.objects.create(user=user, rule=rule, addRule=False)

        self.assertEqual(order1.user, user)
        self.assertEqual(order1.rule, rule)
        self.assertEqual(order1.addRule, True)
        self.assertIsNotNone(order1.creationDate)

        self.assertEqual(order2.addRule, False)

    def test_str(self):
        rule = KeyRule.objects.get(id=1)
        user = rule.key.manager

        obj = KeyRequest.objects.create(user=user, rule=rule)
        self.assertNotEqual(str(obj), '')


class KeyConfirmtTest(TestCase):
    def setUp(self):
        create_KeyOrder()

    def test_basic(self):
        order = KeyOrder.objects.get(id=1)
        user = SysUser.objects.get(id=2)

        confirm = KeyConfirm.objects.create(order=order, user=user)

        self.assertEqual(confirm.user, user)
        self.assertEqual(confirm.order, order)
        self.assertIsNotNone(confirm.executionDate)

    def test_str(self):
        order = KeyOrder.objects.get(id=1)
        user = SysUser.objects.get(id=2)

        obj = KeyConfirm.objects.create(order=order, user=user)
        self.assertNotEqual(str(obj), '')


class PersonGroupTest(TestCase):
    def setUp(self):
        PersonGroup.objects.create(name='Group 1')
        PersonGroup.objects.create(name='Group 2')

    def test_basic(self):
        group1 = PersonGroup.objects.get(name='Group 1')
        group2 = PersonGroup.objects.get(name='Group 2')

        self.assertEqual(group1.name, 'Group 1')
        self.assertEqual(group2.name, 'Group 2')

    def test_str(self):
        obj = PersonGroup.objects.get(name='Group 1')
        self.assertNotEqual(str(obj), '')


class PersonTest(TestCase):
    def setUp(self):
        group1 = PersonGroup.objects.create(name='Group 1')
        group2 = PersonGroup.objects.create(name='Group 2')

        Person.objects.create(firstName='First1',
                              lastName='Last1',
                              isActive=True,
                              cardNumber='123123123',
                              group=group1)
        Person.objects.create(firstName='First2',
                              lastName='Last2',
                              cardNumber='00000000000000001',
                              group=group2)
        Person.objects.create(firstName='First3',
                              lastName='Last3',
                              isActive=False,
                              cardNumber='234255635462452',
                              group=group1)
        Person.objects.create(firstName='',
                              lastName='',
                              cardNumber='1111111111111111111111111111111111111111111',
                              group=group1)

    def test_basic(self):
        group1 = PersonGroup.objects.get(name='Group 1')
        group2 = PersonGroup.objects.get(name='Group 2')

        person1 = Person.objects.get(id=1)
        person2 = Person.objects.get(id=2)
        person3 = Person.objects.get(id=3)
        person4 = Person.objects.get(id=4)

        self.assertEqual(person1.firstName, 'First1')
        self.assertEqual(person1.lastName, 'Last1')
        self.assertEqual(person1.isActive, True)
        self.assertEqual(person1.cardNumber, '123123123')
        self.assertEqual(person1.group, group1)

        self.assertEqual(person2.firstName, 'First2')
        self.assertEqual(person2.lastName, 'Last2')
        self.assertEqual(person2.isActive, True)
        self.assertEqual(person2.cardNumber, '00000000000000001')
        self.assertEqual(person2.group, group2)

        self.assertEqual(person3.firstName, 'First3')
        self.assertEqual(person3.lastName, 'Last3')
        self.assertEqual(person3.isActive, False)
        self.assertEqual(person3.cardNumber, '234255635462452')
        self.assertEqual(person3.group, group1)

        self.assertEqual(person4.firstName, '')
        self.assertEqual(person4.lastName, '')
        self.assertEqual(person4.isActive, True)
        self.assertEqual(person4.cardNumber, '1111111111111111111111111111111111111111111')
        self.assertEqual(person4.group, group1)

    def test_str(self):
        obj = Person.objects.get(id=1)
        self.assertNotEqual(str(obj), '')