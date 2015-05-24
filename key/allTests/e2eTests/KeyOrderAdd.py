# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from key.models import Key, KeyOrder, KeyRule
from users.models import SysUser, Person
from users.allTests.e2eTests.userLogin import create_test_user


class KeyOrderAddTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_keyOrder_add_form(self):
        create_test_user()
        user = SysUser.objects.last()

        fixture = AutoFixture(Key, generate_fk=True)
        key = fixture.create(1)[0]

        fixture = AutoFixture(Person, generate_fk=True)
        person = fixture.create(1)[0]

        self.assertEqual(0,
                         call('nightwatch --test key/allTests/e2eTests/KeyOrderAdd.js', shell=True),
                         'Nighwatch tests failed')
        order = KeyOrder.objects.all()[0]
        rule = KeyRule.objects.all()[0]
        self.assertEqual(order.user, user)
        self.assertEqual(order.rule, rule)
        self.assertEqual(rule.person, person)
        self.assertEqual(rule.key, key)
