# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from key.models import KeyOrder, KeyRequest
from users.models import Person
from users.allTests.e2eTests.userLogin import create_test_user


class KeyRequestAcceptTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_keyRequest_accept(self):
        create_test_user()

        fixture = AutoFixture(KeyRequest, generate_fk=True)
        request = fixture.create(1)[0]
        rule = request.rule

        fixture = AutoFixture(Person, generate_fk=True)
        fixture.create(1)

        self.assertEqual(0,
                         call('nightwatch --test key/allTests/e2eTests/KeyRequestAccept.js', shell=True),
                         'Nighwatch tests failed')
        order = KeyOrder.objects.all()[0]
        # after accepting request we should get order with the same rule
        self.assertEqual(order.rule, rule)
        # request should be deleted
        self.assertEqual(0, KeyRequest.objects.count())
