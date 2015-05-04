# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from alarm.models import AlarmZone, AlarmOrder, AlarmRule, AlarmRequest
from users.models import SysUser, Person
from users.allTests.e2eTests.userLogin import create_test_user


class AlarmRequestAddFromPerson_Deny(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_alarm_request_from_person_page_deny(self):
        create_test_user()
        user_1 = SysUser.objects.last()

        fixture = AutoFixture(SysUser, generate_fk=True)
        user_2 = fixture.create(1)[0]

        fixture = AutoFixture(AlarmZone, generate_fk=True)
        zone = fixture.create(1)[0]
        zone.manager = user_2
        zone.save()

        fixture = AutoFixture(Person, generate_fk=True)
        person = fixture.create(1)[0]

        zone.persons.add(person)

        self.assertEqual(0,
                         call('nightwatch --test alarm/allTests/e2eTests/alarmOrderAddFromPerson2.js', shell=True),
                         'Nighwatch tests failed')

        request = AlarmRequest.objects.all()[0]
        rule = request.rule
        self.assertEqual(request.user, user_1)
        self.assertFalse(request.grant_privilege)
        self.assertEqual(rule.person, person)
        self.assertEqual(rule.zone, zone)
