# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from alarm.models import AlarmZone, AlarmRequest, AlarmRule
from users.models import SysUser, Person
from users.allTests.e2eTests.userLogin import create_test_user


class AlarmRequestAddTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_alarmrequest_add_form(self):
        create_test_user()
        user = SysUser.objects.last()

        fixture = AutoFixture(AlarmZone, generate_fk=True)
        zone = fixture.create(1)[0]

        fixture = AutoFixture(Person, generate_fk=True)
        person = fixture.create(1)[0]

        self.assertEqual(0,
                         call('nightwatch --test alarm/allTests/e2eTests/alarmRequestAdd.js', shell=True),
                         'Nighwatch tests failed')
        request = AlarmRequest.objects.all()[0]
        rule = AlarmRule.objects.all()[0]
        self.assertEqual(request.user, user)
        self.assertEqual(request.rule, rule)
        self.assertEqual(rule.person, person)
        self.assertEqual(rule.zone, zone)
