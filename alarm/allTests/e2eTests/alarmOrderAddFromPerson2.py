# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from alarm.models import AlarmZone, AlarmOrder, AlarmRule, AlarmRequest
from users.models import SysUser, Person
from users.allTests.e2eTests.userLogin import create_test_user


class AlarmOrderAddFromPerson_Deny(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_alarm_order_from_person_page_deny(self):
        create_test_user()
        user = SysUser.objects.last()

        fixture = AutoFixture(AlarmZone, generate_fk=True)
        zone = fixture.create(1)[0]
        zone.manager = user
        zone.save()

        fixture = AutoFixture(Person, generate_fk=True)
        person = fixture.create(1)[0]

        zone.persons.add(person)

        self.assertEqual(0,
                         call('nightwatch --test alarm/allTests/e2eTests/alarmOrderAddFromPerson2.js', shell=True),
                         'Nighwatch tests failed')

        order = AlarmOrder.objects.all()[0]
        rule = order.rule
        self.assertEqual(order.user, user)
        self.assertFalse(order.grant_privilege)
        self.assertEqual(rule.person, person)
        self.assertEqual(rule.zone, zone)
