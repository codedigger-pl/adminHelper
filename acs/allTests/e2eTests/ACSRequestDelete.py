# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from acs.models import ACSRequest, ACSRule
from users.allTests.e2eTests.userLogin import create_test_user


class ACSRequestDeleteTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_ACSrequest_delete(self):
        create_test_user()

        fixture = AutoFixture(ACSRequest, generate_fk=True)
        fixture.create(1)
        self.assertEqual(0,
                         call('nightwatch --test acs/allTests/e2eTests/ACSRequestDelete.js', shell=True),
                         'Nighwatch tests failed')
        self.assertEqual(0, ACSRequest.objects.count())
        self.assertEqual(0, ACSRule.objects.count())
