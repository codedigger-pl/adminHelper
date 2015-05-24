# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from key.models import KeyRequest, KeyRule
from users.allTests.e2eTests.userLogin import create_test_user


class KeyRequestDeleteTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_keyRequest_delete(self):
        create_test_user()

        fixture = AutoFixture(KeyRequest, generate_fk=True)
        fixture.create(1)
        self.assertEqual(0,
                         call('nightwatch --test key/allTests/e2eTests/KeyRequestDelete.js', shell=True),
                         'Nighwatch tests failed')
        self.assertEqual(0, KeyRequest.objects.count())
        self.assertEqual(0, KeyRule.objects.count())
