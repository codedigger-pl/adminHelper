# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from acs.models import ACSOrder, ACSRule
from users.allTests.e2eTests.userLogin import create_test_user


class ACSOrderDeleteTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_ACSorder_delete(self):
        create_test_user()

        fixture = AutoFixture(ACSOrder, generate_fk=True)
        fixture.create(1)
        self.assertEqual(0,
                         call('nightwatch --test acs/allTests/e2eTests/ACSOrderDelete.js', shell=True),
                         'Nighwatch tests failed')
        self.assertEqual(0, ACSOrder.objects.count())
        self.assertEqual(0, ACSRule.objects.count())
