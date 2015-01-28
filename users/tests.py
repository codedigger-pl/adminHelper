#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pep8
from django.test import TestCase


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


class PEP8Test(TestCase):
    """ All PEP8 tests
    """
    def test_pep8(self):
        """ Testing PEP8 """
        pep8style = pep8.StyleGuide(quiet=False, ignore=['E501'])
        result = pep8style.check_files(['users/admin.py', 'users/api.py', 'users/apiSerializers.py', 'users/models.py',
                                        'users/tests.py', 'users/views.py'])
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')
