# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from alarm.models import AlarmOrder, AlarmZone
from users.allTests.e2eTests.userLogin import create_test_user


class AlarmOrderExecuteTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_alarmorder_execute(self):
        create_test_user()

        fixture = AutoFixture(AlarmOrder, generate_fk=True)
        fixture.create(1)
        zone = AlarmZone.objects.all()[0]
        zone.persons.clear()
        zone.save()
        self.assertEqual(0,
                         call('nightwatch --test alarm/allTests/e2eTests/alarmOrderExecute.js', shell=True),
                         'Nighwatch tests failed')
        zone = AlarmZone.objects.all()[0]
        self.assertEqual(1, zone.persons.count())
