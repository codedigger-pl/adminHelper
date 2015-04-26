# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from autofixture import AutoFixture
from subprocess import call

from users.models import PersonGroup, Person
from .userLogin import create_test_user


class PersonDataChangeTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_personDataChange(self):
        create_test_user()
        # creating groups
        group_fixture = AutoFixture(PersonGroup)
        group1, group2 = group_fixture.create(2)
        # creating person with first group
        person_fixture = AutoFixture(Person)
        person, = person_fixture.create(1)
        person.group = group1
        person.save()
        # calling browser
        self.assertEqual(0,
                         call('nightwatch --test users/allTests/e2eTests/personDataChange.js', shell=True),
                         'Nighwatch tests failed')
        person = Person.objects.all()[0]
        self.assertEqual('New first name', person.first_name)
        self.assertEqual('NEW LAST NAME', person.last_name)
        self.assertEqual('pan', person.rank)
        self.assertEqual(group2, person.group)
