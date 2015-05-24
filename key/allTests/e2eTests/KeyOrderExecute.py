# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from key.models import KeyOrder, Key
from users.allTests.e2eTests.userLogin import create_test_user


class KeyOrderExecuteTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_keyOrder_execute(self):
        create_test_user()

        fixture = AutoFixture(KeyOrder, generate_fk=True)
        order = fixture.create(1)[0]
        order.grant_privilege = True
        order.save()

        key = Key.objects.all()[0]
        key.persons.clear()
        key.save()

        self.assertEqual(0,
                         call('nightwatch --test key/allTests/e2eTests/KeyOrderExecute.js', shell=True),
                         'Nighwatch tests failed')

        key = Key.objects.all()[0]
        self.assertEqual(1, key.persons.count())
