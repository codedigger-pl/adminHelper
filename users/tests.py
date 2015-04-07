# -*- coding: utf-8 -*-

from django.test import TestCase
import pep8


# Enabling basic view tests
from .allTests.viewTests.homePage import HomePageTest
from .allTests.viewTests.usersOverview import UsersOverviewTest

# Enabling class tests
from .allTests.classTests.person import PersonClassTest
from .allTests.classTests.personGroup import PersonGroupClassTest

# Enabling API tests
from .allTests.apiTests.person import APIPersonTest, APIPersonsTest_lastItems, APITest_Person_serializerSwitcher
from .allTests.apiTests.personGroup import APIPersonGroupTest, APIPersonGroup_lastItems

# Enabling WEB tests
from .allTests.e2eTests.webTests import WEBTests


class PEP8Test(TestCase):
    """All PEP8 tests"""

    def test_pep8(self):
        """Testing PEP8"""
        pep8style = pep8.StyleGuide(quiet=False, ignore=['E501'])
        result = pep8style.check_files(['users/admin.py', 'users/apiSerializers.py', 'users/models.py',
                                        'users/tests.py', 'users/views.py', 'users/filters.py'])
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')
