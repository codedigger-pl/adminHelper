# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from key.models import Key, KeyRequest
from users.models import SysUser, Person
from users.allTests.e2eTests.userLogin import create_test_user


class KeyRequestAddFromPerson(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_key_request_from_person_page(self):
        create_test_user()
        user_1 = SysUser.objects.last()

        fixture = AutoFixture(SysUser, generate_fk=True)
        user_2 = fixture.create(1)[0]

        fixture = AutoFixture(Key, generate_fk=True)
        key = fixture.create(1)[0]
        key.manager = user_2
        key.save()

        fixture = AutoFixture(Person, generate_fk=True)
        person = fixture.create(1)[0]

        self.assertEqual(0,
                         call('nightwatch --test key/allTests/e2eTests/KeyOrderAddFromPerson.js', shell=True),
                         'Nighwatch tests failed')

        request = KeyRequest.objects.all()[0]
        rule = request.rule
        self.assertEqual(request.user, user_1)
        self.assertTrue(request.grant_privilege)
        self.assertEqual(rule.person, person)
        self.assertEqual(rule.key, key)
