# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from acs.models import ACSZone, ACSOrder, ACSRule, ACSRequest
from users.models import SysUser, Person
from users.allTests.e2eTests.userLogin import create_test_user


class ACSOrderAddFromPerson_Deny(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_ACS_order_from_person_page_deny(self):
        create_test_user()
        user = SysUser.objects.last()

        fixture = AutoFixture(ACSZone, generate_fk=True)
        zone = fixture.create(1)[0]
        zone.manager = user
        zone.save()

        fixture = AutoFixture(Person, generate_fk=True)
        person = fixture.create(1)[0]

        zone.persons.add(person)

        self.assertEqual(0,
                         call('nightwatch --test acs/allTests/e2eTests/ACSOrderAddFromPerson2.js', shell=True),
                         'Nighwatch tests failed')

        order = ACSOrder.objects.all()[0]
        rule = order.rule
        self.assertEqual(order.user, user)
        self.assertFalse(order.grant_privilege)
        self.assertEqual(rule.person, person)
        self.assertEqual(rule.zone, zone)
