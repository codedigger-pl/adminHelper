# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from key.models import Key, KeyRequest, KeyRule
from users.models import SysUser, Person
from users.allTests.e2eTests.userLogin import create_test_user


class KeyRequestAddTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_kyeRequest_add_form(self):
        create_test_user()
        user = SysUser.objects.last()

        fixture = AutoFixture(Key, generate_fk=True)
        key = fixture.create(1)[0]

        fixture = AutoFixture(Person, generate_fk=True)
        person = fixture.create(1)[0]

        self.assertEqual(0,
                         call('nightwatch --test key/allTests/e2eTests/KeyRequestAdd.js', shell=True),
                         'Nighwatch tests failed')
        request = KeyRequest.objects.all()[0]
        rule = KeyRule.objects.all()[0]
        self.assertEqual(request.user, user)
        self.assertEqual(request.rule, rule)
        self.assertEqual(rule.person, person)
        self.assertEqual(rule.key, key)
