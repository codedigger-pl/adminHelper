#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pep8
from django.test import TestCase
from autofixture import AutoFixture

from .models import PersonGroup, Person


class HomePageTest(TestCase):
    """ All tests about Home Page
    """
    def test_access(self):
        """ Testing access to home page """
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)


class UsersPageTest(TestCase):
    """ All tests to users page ('/users/*')
    """
    def test_access_overview(self):
        """ Testing access to users overview page """
        resp = self.client.get('/users/overview')
        self.assertEqual(resp.status_code, 200)


class APITest(TestCase):
    """ All API tests
    """
    def test_access_persons(self):
        """ Testing access to persons API values
        """
        resp = self.client.get('/api/users/persons/')
        self.assertEqual(resp.status_code, 200)

    def test_access_personGroups(self):
        """ Testing access to persons API values
        """
        resp = self.client.get('/api/users/personGroups/')
        self.assertEqual(resp.status_code, 200)

    def test_random_personGroups_access(self):
        """ Testing access to random created PersonGroup objects
        """
        fixture = AutoFixture(PersonGroup)
        fixture.create(20)
        for i in range(1, 21):
            resp = self.client.get('/api/users/personGroups/' + str(i) + '/')
            self.assertEqual(resp.status_code, 200)

    def test_random_persons_access(self):
        """ Testing access to random created Person objects
        """
        fixture = AutoFixture(Person, generate_fk=True)
        fixture.create(20)
        for i in range(1, 21):
            resp = self.client.get('/api/users/persons/' + str(i) + '/')
            self.assertEqual(resp.status_code, 200)


class PEP8Test(TestCase):
    """ All PEP8 tests
    """
    def test_pep8(self):
        """ Testing PEP8 """
        pep8style = pep8.StyleGuide(quiet=False, ignore=['E501'])
        result = pep8style.check_files(['users/admin.py', 'users/api.py', 'users/apiSerializers.py', 'users/models.py',
                                        'users/tests.py', 'users/views.py'])
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')
