# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from autofixture import AutoFixture
from subprocess import call

from users.models import PersonGroup, Person

class PersonCardNumberChangeTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_personCardNumberChangeForm(self):
        # creating groups
        group_fixture = AutoFixture(PersonGroup)
        group_fixture.create(1)
        # creating person with first group
        person_fixture = AutoFixture(Person)
        person_fixture.create(1)
        # calling browser
        self.assertEqual(0,
                         call('cd users/allTests/e2eTests && nightwatch --test personCardNumberChange.js', shell=True),
                         'Nighwatch tests failed')
        person = Person.objects.all()[0]
        self.assertEqual(person.card_number, '2222222222')
