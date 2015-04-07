# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from autofixture import AutoFixture
from subprocess import call

from users.models import PersonGroup, Person, SysUser

class WEBTests(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_001_pgroupAddForm(self):
        call('cd users/allTests && nightwatch --test forms/pgroupAddForm.js', shell=True)
        # strange: get(id=1) isn't working
        group = PersonGroup.objects.all()[0]
        self.assertEqual(group.name, 'Group name')
        self.assertEqual(group.description, 'This is some group description')

    def test_002_personAddForm(self):
        fixture = AutoFixture(PersonGroup)
        fixture.create(1)
        group = PersonGroup.objects.all()[0]
        call('cd users/allTests && nightwatch --test forms/personAddForm.js', shell=True)
        person = Person.objects.all()[0]
        self.assertEqual(person.first_name, 'First name')
        self.assertEqual(person.last_name, 'LAST NAME')
        self.assertEqual(person.rank, 'kpr.')
        self.assertEqual(person.card_number, '1111111111111')
        self.assertEqual(person.group, group)

    def test_003_personDataChangeForm(self):
        # creating groups
        group_fixture = AutoFixture(PersonGroup)
        group_fixture.create(2)
        # creating person with first group
        person_fixture = AutoFixture(Person)
        person_fixture.create(1)
        person = Person.objects.all()[0]
        person.group = PersonGroup.objects.all()[0]
        person.save()
        # calling browser
        call('cd users/allTests && nightwatch --test forms/personDataChange.js', shell=True)
        person = Person.objects.all()[0]
        self.assertEqual(person.first_name, 'New first name')
        self.assertEqual(person.last_name, 'NEW LAST NAME')
        self.assertEqual(person.rank, 'pan')
        self.assertEqual(person.group, PersonGroup.objects.all()[1])

    def test_004_personCardNumberChangeForm(self):
        # creating groups
        group_fixture = AutoFixture(PersonGroup)
        group_fixture.create(1)
        # creating person with first group
        person_fixture = AutoFixture(Person)
        person_fixture.create(1)
        person = Person.objects.all()[0]
        # calling browser
        call('cd users/allTests && nightwatch --test forms/personCardNumberChange.js', shell=True)
        person = Person.objects.all()[0]
        self.assertEqual(person.card_number, '2222222222')

    def test_005_userAddForm(self):
        # calling browser
        call('cd users/allTests && nightwatch --test forms/userAddForm.js', shell=True)
        user = SysUser.objects.all()[0]
        self.assertEqual(user.username, 'username')
        self.assertEqual(user.first_name, 'First name')
        self.assertEqual(user.last_name, 'Last name')
        self.assertEqual(user.rank, 'kpr.')
        self.assertEqual(user.email, 'user@user.com')