# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from acs.models import ACSOrder, ACSRequest
from users.models import Person
from users.allTests.e2eTests.userLogin import create_test_user


class ACSRequestAcceptTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_ACSrequest_accept(self):
        create_test_user()

        fixture = AutoFixture(ACSRequest, generate_fk=True)
        request = fixture.create(1)[0]
        rule = request.rule

        fixture = AutoFixture(Person, generate_fk=True)
        fixture.create(1)

        self.assertEqual(0,
                         call('nightwatch --test acs/allTests/e2eTests/ACSRequestAccept.js', shell=True),
                         'Nighwatch tests failed')
        order = ACSOrder.objects.all()[0]
        # after accepting request we should get order with the same rule
        self.assertEqual(order.rule, rule)
        # request should be deleted
        self.assertEqual(0, ACSRequest.objects.count())
