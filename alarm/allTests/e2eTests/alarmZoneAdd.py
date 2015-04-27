# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call

from alarm.models import AlarmZone
from users.allTests.e2eTests.userLogin import create_test_user


class AlarmZoneAddTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_alarmzone_add_form(self):
        create_test_user()
        self.assertEqual(0,
                         call('nightwatch --test alarm/allTests/e2eTests/alarmZoneAdd.js', shell=True),
                         'Nighwatch tests failed')
        zone = AlarmZone.objects.all()[0]
        self.assertEqual(zone.name, 'Zone name')
        self.assertEqual(zone.description, 'Zone description')
        self.assertIsNotNone(zone.manager)
