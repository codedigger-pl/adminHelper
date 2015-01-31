#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pep8
from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from autofixture import AutoFixture

from .models import PersonGroup, Person


class HomePageTest(TestCase):
    """ All tests about Home Page
    """
    def test_access(self):
        """ Testing access to home page """
        resp = self.client.get(reverse('homepage'))
        self.assertEqual(resp.status_code, 200)


class UsersPageTest(TestCase):
    """ All tests to users page ('/users/*')
    """
    def test_access_overview(self):
        """ Testing access to users overview page """
        resp = self.client.get(reverse('usersOverview'))
        self.assertEqual(resp.status_code, 200)


class APITest(APITestCase):
    """ All API tests
    """
    def test_access_persons(self):
        """Testing access to persons API values"""
        resp = self.client.get(reverse('api:person-list'))
        self.assertEqual(resp.status_code, 200)

    def test_access_personGroups(self):
        """Testing access to persons API values"""
        resp = self.client.get(reverse('api:persongroup-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_personGroups_access(self):
        """Testing access to random created PersonGroup objects"""
        fixture = AutoFixture(PersonGroup)
        fixture.create(20)
        for i in range(1, 21):
            resp = self.client.get(reverse('api:persongroup-list') + str(i) + '/')
            self.assertEqual(resp.status_code, 200)

    def test_random_persons_access(self):
        """Testing access to random created Person objects"""
        fixture = AutoFixture(Person, generate_fk=True)
        fixture.create(20)
        for i in range(1, 21):
            resp = self.client.get(reverse('api:person-list') + str(i) + '/')
            self.assertEqual(resp.status_code, 200)

    def test_persons_last_items(self):
        """Testing access to some last persons"""
        fixture = AutoFixture(Person, generate_fk=True)
        personsGenerated = fixture.create(20)[-5:]
        resp = self.client.get(reverse('api:person-list') + '?onlyLastItems=5')
        for (i, person) in enumerate(resp.data):
            # checking only id field.
            # If this is correct and other fields aren't, something wrong is happening in serializer
            self.assertEqual(personsGenerated[i].id, person['id'])


class PEP8Test(TestCase):
    """All PEP8 tests"""
    def test_pep8(self):
        """Testing PEP8"""
        pep8style = pep8.StyleGuide(quiet=False, ignore=['E501'])
        result = pep8style.check_files(['users/admin.py', 'users/api.py', 'users/apiSerializers.py', 'users/models.py',
                                        'users/tests.py', 'users/views.py'])
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')
