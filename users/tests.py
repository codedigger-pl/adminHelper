# -*- coding: utf-8 -*-

from django.test import TestCase
import pep8

ENABLE_E2E_TESTS = False

# Enabling basic view tests
from .allTests.viewTests.homePage import HomePageTest
from .allTests.viewTests.usersOverview import UsersOverviewTest
from .allTests.viewTests.personGroup import PersonGroupTest
from .allTests.viewTests.login import LoginTest

# Enabling class tests
from .allTests.classTests.person import PersonClassTest
from .allTests.classTests.personGroup import PersonGroupClassTest

# Enabling API tests
from .allTests.apiTests.person import APIPersonTest, APIPersonsTest_lastItems, APITest_Person_serializerSwitcher
from .allTests.apiTests.personGroup import APIPersonGroupTest, APIPersonGroup_lastItems
from .allTests.apiTests.sysUser import APISysUserTest

# Enabling WEB tests
if ENABLE_E2E_TESTS:
    from .allTests.e2eTests.personAddForm import PersonAddFormTest
    from .allTests.e2eTests.personDataChange import PersonDataChangeTest
    from .allTests.e2eTests.personCardNumberChange import PersonCardNumberChangeTest
    from .allTests.e2eTests.pgroupAddForm import PersonGroupAddFormTest
    from .allTests.e2eTests.userAddForm import UserAddFormTest
    from .allTests.e2eTests.personGroupDataChange import PersonGroupDataChangeTest
    from .allTests.e2eTests.userLogin import UserLoginTest


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
        files_prefix = 'users/'
        files = ['admin.py',
                 'apiSerializers.py',
                 'apiViewsets.py',
                 'models.py',
                 'tests.py',
                 'views.py',
                 'filters.py']
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')

    def test_tests_apiTests(self):
        """Testing apiTests files"""
        files_prefix = 'users/allTests/apiTests/'
        files = []
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')

    def test_tests_classTests(self):
        """Testing classTests files"""
        files_prefix = 'users/allTests/classTests/'
        files = []
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')

    def test_tests_e2eTests(self):
        """Testing e2eTests files"""
        files_prefix = 'users/allTests/e2eTests/'
        files = []
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')

    def test_tests_viewTests(self):
        """Testing viewTests files"""
        files_prefix = 'users/allTests/viewTests/'
        files = []
        result = self.check_PEP8_file(files_prefix, files)
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')
