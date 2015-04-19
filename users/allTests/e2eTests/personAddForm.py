# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from autofixture import AutoFixture
from subprocess import call

from users.models import PersonGroup, Person


class PersonAddFormTest(StaticLiveServerTestCase):

    def test_personAddForm(self):
        fixture = AutoFixture(PersonGroup)
        group = fixture.create(1)[0]
        self.assertEqual(0,
                         call('nightwatch --test users/allTests/e2eTests/personAddForm.js', shell=True),
                         'Nighwatch tests failed')
        person = Person.objects.all()[0]
        self.assertEqual(person.first_name, 'First name')
        self.assertEqual(person.last_name, 'LAST NAME')
        self.assertEqual(person.rank, 'kpr.')
        self.assertEqual(person.card_number, '1111111111111')
        self.assertEqual(person.group, group)
