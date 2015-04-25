# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from alarm.models import AlarmOrder, AlarmRequest, AlarmRule
from users.models import SysUser, Person


class AlarmRequestAcceptTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_alarmrequest_accept_form(self):
        fixture = AutoFixture(SysUser, generate_fk=True)
        fixture.create(1)

        fixture = AutoFixture(AlarmRequest, generate_fk=True)
        request = fixture.create(1)[0]
        rule = request.rule

        fixture = AutoFixture(Person, generate_fk=True)
        fixture.create(1)

        self.assertEqual(0,
                         call('nightwatch --test alarm/allTests/e2eTests/alarmRequestAccept.js', shell=True),
                         'Nighwatch tests failed')
        order = AlarmOrder.objects.all()[0]
        # after accepting request we should get order with the same rule
        self.assertEqual(order.rule, rule)
        # request should be deleted
        self.assertEqual(0, AlarmRequest.objects.count())
