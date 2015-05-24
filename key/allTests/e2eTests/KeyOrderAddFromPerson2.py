# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from key.models import Key, KeyOrder
from users.models import SysUser, Person
from users.allTests.e2eTests.userLogin import create_test_user


class KeyOrderAddFromPerson_Deny(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_key_order_from_person_page_deny(self):
        create_test_user()
        user = SysUser.objects.last()

        fixture = AutoFixture(Key, generate_fk=True)
        key = fixture.create(1)[0]
        key.manager = user
        key.save()

        fixture = AutoFixture(Person, generate_fk=True)
        person = fixture.create(1)[0]

        key.persons.add(person)

        self.assertEqual(0,
                         call('nightwatch --test key/allTests/e2eTests/KeyOrderAddFromPerson2.js', shell=True),
                         'Nighwatch tests failed')

        order = KeyOrder.objects.all()[0]
        rule = order.rule
        self.assertEqual(order.user, user)
        self.assertFalse(order.grant_privilege)
        self.assertEqual(rule.person, person)
        self.assertEqual(rule.key, key)
