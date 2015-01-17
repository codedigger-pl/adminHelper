#!/usr/bin/env python

# -*- coding: utf-8 -*-


from django.test import TestCase

from users.models import SysUser, Person, PersonGroup

from .models import Key, KeyConfirm, KeyOrder, KeyRequest, KeyRule

# some basic class creators
def create_SysUser1(): return SysUser.objects.create_user(username='Manager 1')

def create_PersonGroup1(): return PersonGroup.objects.create(name='Group 1')
def create_Person1(): return Person.objects.create(firstName='First name',
                                                   lastName='Last name',
                                                   isActive=True,
                                                   cardNumber='123',
                                                   group=create_PersonGroup1())

def create_Key1(): return Key.objects.create(name='Key 1', manager=create_SysUser1())
def create_KeyRule1(): return KeyRule.objects.create(person=create_Person1(), key=create_Key1())
def create_KeyOrder(): return KeyOrder.objects.create(rule=create_KeyRule1(),
                                                      user=SysUser.objects.create_user(username='Manager 2'))


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