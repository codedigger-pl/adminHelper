# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call

from acs.models import ACSZone
from users.allTests.e2eTests.userLogin import create_test_user


class ACSZoneAddTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_ACSzone_add_form(self):
        create_test_user()
        self.assertEqual(0,
                         call('nightwatch --test acs/allTests/e2eTests/ACSZoneAdd.js', shell=True),
                         'Nighwatch tests failed')
        zone = ACSZone.objects.all()[0]
        self.assertEqual(zone.name, 'Zone name')
        self.assertEqual(zone.description, 'Zone description')
        self.assertIsNotNone(zone.manager)
