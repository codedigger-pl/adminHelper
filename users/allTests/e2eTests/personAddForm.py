# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from autofixture import AutoFixture
from subprocess import call

from users.models import PersonGroup, Person


class PersonAddFormTest(StaticLiveServerTestCase):

    def test_personAddForm(self):
        fixture = AutoFixture(PersonGroup)
        group = fixture.create(1)[0]
        call('cd users/allTests/e2eTests && nightwatch --test personAddForm.js', shell=True)
        person = Person.objects.all()[0]
        self.assertEqual(person.first_name, 'First name')
        self.assertEqual(person.last_name, 'LAST NAME')
        self.assertEqual(person.rank, 'kpr.')
        self.assertEqual(person.card_number, '1111111111111')
        self.assertEqual(person.group, group)
