# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from alarm.models import AlarmZone
from users.models import SysUser


class AlarmZoneAddTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_pgroupAddForm(self):
        fixture = AutoFixture(SysUser, generate_fk=True)
        fixture.create(1)
        self.assertEqual(0,
                         call('nightwatch --test alarm/allTests/e2eTests/alarmZoneAdd.js', shell=True),
                         'Nighwatch tests failed')
        zone = AlarmZone.objects.all()[0]
        self.assertEqual(zone.name, 'Zone name')
        self.assertEqual(zone.description, 'Zone description')
        self.assertIsNotNone(zone.manager)
