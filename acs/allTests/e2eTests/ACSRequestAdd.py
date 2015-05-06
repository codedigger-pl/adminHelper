# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from acs.models import ACSZone, ACSRequest, ACSRule
from users.models import SysUser, Person
from users.allTests.e2eTests.userLogin import create_test_user


class ACSRequestAddTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_ACSrequest_add_form(self):
        create_test_user()
        user = SysUser.objects.last()

        fixture = AutoFixture(ACSZone, generate_fk=True)
        zone = fixture.create(1)[0]

        fixture = AutoFixture(Person, generate_fk=True)
        person = fixture.create(1)[0]

        self.assertEqual(0,
                         call('nightwatch --test acs/allTests/e2eTests/ACSRequestAdd.js', shell=True),
                         'Nighwatch tests failed')
        request = ACSRequest.objects.all()[0]
        rule = ACSRule.objects.all()[0]
        self.assertEqual(request.user, user)
        self.assertEqual(request.rule, rule)
        self.assertEqual(rule.person, person)
        self.assertEqual(rule.zone, zone)
