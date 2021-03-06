# -*- coding: utf-8 -*-

from django.test import TestCase
import pep8

ENABLE_E2E_TESTS = True

# Enabling class tests
from .allTests.classTests.alarmZone import AlarmZoneTest
from .allTests.classTests.alarmOrder import AlarmOrderTest
from .allTests.classTests.alarmRequest import AlarmRequestTest

# Enabling basic view tests
from .allTests.viewTests.alarmOverview import AlarmOverviewTest
from .allTests.viewTests.alarmZone import AddAlarmZoneTest
from .allTests.viewTests.alarmOrder import AddAlarmOrderTest
from .allTests.viewTests.alarmRequest import AddAlarmRequestrTest

# Enabling API tests
from .allTests.apiTests.alarmZone import APIAlarmZoneTest
from .allTests.apiTests.alarmOrder import APIAlarmOrderTest
from .allTests.apiTests.alarmRule import APIAlarmRuleTest
from .allTests.apiTests.alarmRequest import APIAlarmRequestTest

# Enabling WEB tests
if ENABLE_E2E_TESTS:
    from .allTests.e2eTests.alarmZoneAdd import AlarmZoneAddTest
    from .allTests.e2eTests.alarmOrderAdd import AlarmOrderAddTest
    from .allTests.e2eTests.alarmRequestAdd import AlarmRequestAddTest
    from .allTests.e2eTests.alarmRequestAccept import AlarmRequestAcceptTest
    from .allTests.e2eTests.alarmRequestDelete import AlarmRequestDeleteTest
    from .allTests.e2eTests.alarmOrderDelete import AlarmOrderDeleteTest
    from .allTests.e2eTests.alarmOrderExecute import AlarmOrderExecuteTest
    from .allTests.e2eTests.alarmOrderAddFromPerson import AlarmOrderAddFromPerson
    from .allTests.e2eTests.alarmRequestAddFromPerson import AlarmRequestAddFromPerson
    from .allTests.e2eTests.alarmRequestAddFromPerson2 import AlarmRequestAddFromPerson_Deny
    from .allTests.e2eTests.alarmOrderAddFromPerson2 import AlarmOrderAddFromPerson_Deny


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
        files_prefix = 'alarm/'
        files = ['admin.py',
                 'models.py',
                 'tests.py',
                 'views.py', ]
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')

    def test_tests_apiTests(self):
        """Testing apiTests files"""
        files_prefix = 'alarm/allTests/apiTests/'
        files = []
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')

    def test_tests_classTests(self):
        """Testing classTests files"""
        files_prefix = 'alarm/allTests/classTests/'
        files = []
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')

    def test_tests_e2eTests(self):
        """Testing e2eTests files"""
        files_prefix = 'alarm/allTests/e2eTests/'
        files = []
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')

    def test_tests_viewTests(self):
        """Testing viewTests files"""
        files_prefix = 'alarm/allTests/viewTests/'
        files = []
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')
