#!/usr/bin/env python

# -*- coding: utf-8 -*-


from django.test import TestCase

from .models import Person, PersonGroup, SysUser

# some basic class creators
def create_SysUser1(): return SysUser.objects.create_user(username='Manager 1')

def create_PersonGroup1(): return PersonGroup.objects.create(name='Group 1')
def create_Person1(): return Person.objects.create(firstName='First name',
                                                   lastName='Last name',
                                                   isActive=True,
                                                   cardNumber='123',
                                                   group=create_PersonGroup1())


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