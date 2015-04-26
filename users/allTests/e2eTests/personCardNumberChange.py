# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from autofixture import AutoFixture
from subprocess import call

from users.models import PersonGroup, Person
from .userLogin import create_test_user


class PersonCardNumberChangeTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_personCardNumberChangeForm(self):
        create_test_user()
        # creating groups
        group_fixture = AutoFixture(PersonGroup)
        group_fixture.create(1)
        # creating person with first group
        person_fixture = AutoFixture(Person)
        person_fixture.create(1)
        # calling browser
        self.assertEqual(0,
                         call('nightwatch --test users/allTests/e2eTests/personCardNumberChange.js', shell=True),
                         'Nighwatch tests failed')
        person = Person.objects.all()[0]
        self.assertEqual(person.card_number, '2222222222')
