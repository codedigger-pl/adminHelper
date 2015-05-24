# -*- coding: utf-8 -*-

from django.test import TestCase
import pep8

ENABLE_E2E_TESTS = True

# Enabling class tests
from .allTests.classTests.Key import KeyTest
from .allTests.classTests.KeyOrder import KeyOrderTest
from .allTests.classTests.KeyRequest import KeyRequestTest

# Enabling basic view tests
from .allTests.viewTests.KeyOverview import KeyOverviewTest
from .allTests.viewTests.Key import AddKeyTest
from .allTests.viewTests.KeyOrder import AddKeyOrderTest
from .allTests.viewTests.KeyRequest import AddKeyRequestrTest

# Enabling API tests
from .allTests.apiTests.KeyZone import APIKeyZoneTest
from .allTests.apiTests.KeyOrder import APIKeyOrderTest
from .allTests.apiTests.KeyRule import APIKeyRuleTest
from .allTests.apiTests.KeyRequest import APIKeyRequestTest

# Enabling WEB tests
if ENABLE_E2E_TESTS:
    from .allTests.e2eTests.KeyAdd import KeyAddTest
    from .allTests.e2eTests.KeyOrderAdd import KeyOrderAddTest
    from .allTests.e2eTests.KeyRequestAdd import KeyRequestAddTest
    from .allTests.e2eTests.KeyRequestAccept import KeyRequestAcceptTest
    from .allTests.e2eTests.KeyRequestDelete import KeyRequestDeleteTest
    from .allTests.e2eTests.KeyOrderDelete import KeyOrderDeleteTest
    from .allTests.e2eTests.KeyOrderExecute import KeyOrderExecuteTest
    from .allTests.e2eTests.KeyOrderAddFromPerson import KeyOrderAddFromPerson
    from .allTests.e2eTests.KeyRequestAddFromPerson import KeyRequestAddFromPerson
    from .allTests.e2eTests.KeyRequestAddFromPerson2 import KeyRequestAddFromPerson_Deny
    from .allTests.e2eTests.KeyOrderAddFromPerson2 import KeyOrderAddFromPerson_Deny


class PEP8Test(TestCase):
    """All PEP8 tests"""

    def check_PEP8_file(self, prefix, file_name):
        pep8style = pep8.StyleGuide(quiet=False, ignore=['E501', 'E402'])
        files = []
        for f in file_name:
            files.append(prefix + f)
        return pep8style.check_files(files)

    def test_users_files(self):
        """Testing main package files"""
        files_prefix = 'key/'
        files = ['admin.py',
                 'models.py',
                 'tests.py',
                 'views.py', ]
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')

    def test_tests_apiTests(self):
        """Testing apiTests files"""
        files_prefix = 'key/allTests/apiTests/'
        files = []
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')

    def test_tests_classTests(self):
        """Testing classTests files"""
        files_prefix = 'key/allTests/classTests/'
        files = []
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')

    def test_tests_e2eTests(self):
        """Testing e2eTests files"""
        files_prefix = 'key/allTests/e2eTests/'
        files = []
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')

    def test_tests_viewTests(self):
        """Testing viewTests files"""
        files_prefix = 'key/allTests/viewTests/'
        files = []
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')
