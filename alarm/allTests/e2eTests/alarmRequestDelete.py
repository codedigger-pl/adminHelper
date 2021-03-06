# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from alarm.models import AlarmRequest, AlarmRule
from users.allTests.e2eTests.userLogin import create_test_user


class AlarmRequestDeleteTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_alarmrequest_delete(self):
        create_test_user()

        fixture = AutoFixture(AlarmRequest, generate_fk=True)
        fixture.create(1)
        self.assertEqual(0,
                         call('nightwatch --test alarm/allTests/e2eTests/alarmRequestDelete.js', shell=True),
                         'Nighwatch tests failed')
        self.assertEqual(0, AlarmRequest.objects.count())
        self.assertEqual(0, AlarmRule.objects.count())
