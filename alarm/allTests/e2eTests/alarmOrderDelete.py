# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from alarm.models import AlarmOrder, AlarmRequest, AlarmRule
from users.models import SysUser, Person
from users.allTests.e2eTests.userLogin import create_test_user


class AlarmOrderDeleteTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_alarmrequest_accept_form(self):
        create_test_user()

        fixture = AutoFixture(AlarmOrder, generate_fk=True)
        fixture.create(1)
        self.assertEqual(0,
                         call('nightwatch --test alarm/allTests/e2eTests/alarmOrderDelete.js', shell=True),
                         'Nighwatch tests failed')
        self.assertEqual(0, AlarmOrder.objects.count())
        self.assertEqual(0, AlarmRule.objects.count())
