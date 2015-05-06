# -*- coding: utf-8 -*-

from django.test import TestCase
import pep8

ENABLE_E2E_TESTS = True

# Enabling class tests
from .allTests.classTests.ACSZone import ACSZoneTest
from .allTests.classTests.ACSOrder import ACSOrderTest
from .allTests.classTests.ACSRequest import ACSRequestTest

# Enabling basic view tests
from .allTests.viewTests.ACSOverview import ACSOverviewTest
from .allTests.viewTests.ACSZone import AddACSZoneTest
from .allTests.viewTests.ACSOrder import AddACSOrderTest
from .allTests.viewTests.ACSRequest import AddACSRequestrTest

# Enabling API tests
from .allTests.apiTests.ACSZone import APIACSZoneTest
from .allTests.apiTests.ACSOrder import APIACSOrderTest
from .allTests.apiTests.ACSRule import APIACSRuleTest
from .allTests.apiTests.ACSRequest import APIACSRequestTest

# Enabling WEB tests
if ENABLE_E2E_TESTS:
    from .allTests.e2eTests.ACSZoneAdd import ACSZoneAddTest
    from .allTests.e2eTests.ACSOrderAdd import ACSOrderAddTest
    from .allTests.e2eTests.ACSRequestAdd import ACSRequestAddTest
    from .allTests.e2eTests.ACSRequestAccept import ACSRequestAcceptTest
    from .allTests.e2eTests.ACSRequestDelete import ACSRequestDeleteTest
    from .allTests.e2eTests.ACSOrderDelete import ACSOrderDeleteTest
    from .allTests.e2eTests.ACSOrderExecute import ACSOrderExecuteTest
    from .allTests.e2eTests.ACSOrderAddFromPerson import ACSOrderAddFromPerson
    from .allTests.e2eTests.ACSRequestAddFromPerson import ACSRequestAddFromPerson
    from .allTests.e2eTests.ACSRequestAddFromPerson2 import ACSRequestAddFromPerson_Deny
    from .allTests.e2eTests.ACSOrderAddFromPerson2 import ACSOrderAddFromPerson_Deny


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
        files_prefix = 'acs/'
        files = ['admin.py',
                 'models.py',
                 'tests.py',
                 'views.py', ]
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')

    def test_tests_apiTests(self):
        """Testing apiTests files"""
        files_prefix = 'acs/allTests/apiTests/'
        files = []
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')

    def test_tests_classTests(self):
        """Testing classTests files"""
        files_prefix = 'acs/allTests/classTests/'
        files = []
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')

    def test_tests_e2eTests(self):
        """Testing e2eTests files"""
        files_prefix = 'acs/allTests/e2eTests/'
        files = []
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')

    def test_tests_viewTests(self):
        """Testing viewTests files"""
        files_prefix = 'acs/allTests/viewTests/'
        files = []
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')
