# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from acs.models import ACSOrder, ACSZone
from users.allTests.e2eTests.userLogin import create_test_user


class ACSOrderExecuteTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_ACSorder_execute(self):
        create_test_user()

        fixture = AutoFixture(ACSOrder, generate_fk=True)
        order = fixture.create(1)[0]
        order.grant_privilege = True
        order.save()

        zone = ACSZone.objects.all()[0]
        zone.persons.clear()
        zone.save()

        self.assertEqual(0,
                         call('nightwatch --test acs/allTests/e2eTests/ACSOrderExecute.js', shell=True),
                         'Nighwatch tests failed')

        zone = ACSZone.objects.all()[0]
        self.assertEqual(1, zone.persons.count())
