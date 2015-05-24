# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call

from key.models import Key
from users.allTests.e2eTests.userLogin import create_test_user


class KeyAddTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_key_add_form(self):
        create_test_user()
        self.assertEqual(0,
                         call('nightwatch --test key/allTests/e2eTests/KeyAdd.js', shell=True),
                         'Nighwatch tests failed')
        key = Key.objects.all()[0]
        self.assertEqual(key.name, 'Key name')
        self.assertEqual(key.description, 'Key description')
        self.assertIsNotNone(key.manager)
