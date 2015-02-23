# -*- coding: utf-8 -*-

import pep8

from subprocess import call
import os
from time import sleep

from django.utils import timezone
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from autofixture import AutoFixture

from .models import PersonGroup, Person, SysUser


class HomePageTest(TestCase):
    """ All tests about Home Page
    """
    def test_access(self):
        """ Testing access to home page """
        resp = self.client.get(reverse('homepage'))
        self.assertEqual(resp.status_code, 200)


class UsersPageTest(TestCase):
    """ All tests to users page ('/users/*')
    """
    def test_access_overview(self):
        """ Testing access to users overview page """
        resp = self.client.get(reverse('usersOverview'))
        self.assertEqual(resp.status_code, 200)


class PersonClassTest(TestCase):
    """ All test for class Person.
    """
    def test_last_name_uppercase(self):
        fixture = AutoFixture(Person, generate_fk=True)
        fixture.create(1)
        person = Person.objects.get(id=1)
        self.assertEqual(str(person.last_name).isupper(), True)

    def test_get_creation_date_properties(self):
        """ Testing correct date and time returning from creation_date field
        :return:
        """
        fixture = AutoFixture(Person, generate_fk=True)
        fixture.create(1)
        person = Person.objects.get(id=1)
        someDate = timezone.now()
        person.creation_date = someDate
        person.save()
        self.assertEqual(someDate.date(), person.creation_date_date)
        self.assertEqual(someDate.time(), person.creation_date_time)


class PersonGroupClassTest(TestCase):
    """ All test for PersonGroup class
    """
    def test_get_creation_date_properties(self):
        """ Testing correct date and time returning from creation_date field
        :return:
        """
        fixture = AutoFixture(PersonGroup)
        fixture.create(1)
        group = PersonGroup.objects.get(id=1)
        someDate = timezone.now()
        group.creation_date = someDate
        group.save()
        self.assertEqual(someDate.date(), group.creation_date_date)
        self.assertEqual(someDate.time(), group.creation_date_time)


class APITest(APITestCase):
    """All primary API tests"""

    def test_access_persons(self):
        """Testing access to persons API values"""
        resp = self.client.get(reverse('api:person-list'))
        self.assertEqual(resp.status_code, 200)

    def test_access_personGroups(self):
        """Testing access to persons API values"""
        resp = self.client.get(reverse('api:persongroup-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_personGroups_access(self):
        """Testing access to random created PersonGroup objects"""
        fixture = AutoFixture(PersonGroup)
        fixture.create(20)
        for i in range(1, 21):
            resp = self.client.get('/'.join([reverse('api:persongroup-list'),
                                             str(i)]))
            self.assertEqual(resp.status_code, 200)

    def test_random_persons_access(self):
        """Testing access to random created Person objects"""
        fixture = AutoFixture(Person, generate_fk=True)
        fixture.create(20)
        for i in range(1, 21):
            resp = self.client.get('/'.join([reverse('api:person-list'),
                                             str(i)]))
            self.assertEqual(resp.status_code, 200)


class APITest_Persons_last(APITestCase):
    """Class for testing Person - last items API requests"""

    def test_last_items(self):
        """Testing access to some last persons - primary use"""
        fixture = AutoFixture(Person, generate_fk=True)
        personsGenerated = fixture.create(20)[-5:]
        resp = self.client.get(reverse('api:person-list') + '?onlyLastItems=5')
        for (i, person) in enumerate(resp.data):
            # checking only id field.
            # If this is correct and other fields aren't, something wrong is happening in serializer
            self.assertEqual(personsGenerated[i].id, person['id'])

    def test_empty_database(self):
        """Testing access to last persons, when database is empty"""
        resp = self.client.get(reverse('api:person-list') + '?onlyLastItems=5')
        self.assertEqual(resp.data, [])

    def test_not_enough(self):
        """Testing last persons, when in database isn't enough data"""
        fixture = AutoFixture(Person, generate_fk=True)
        personsGenerated = fixture.create(5)
        resp = self.client.get(reverse('api:person-list') + '?onlyLastItems=20')
        self.assertEqual(len(resp.data), len(personsGenerated))


class APITest_Person_serializerSwitcher(APITestCase):
    """Class for testing various serializer switching"""

    def test_minimal_serializer(self):
        """Checking, if minimal information present"""
        fixture = AutoFixture(Person, generate_fk=True)
        fixture.create(5)
        resp = self.client.get(reverse('api:person-list') + '?modelType=minimal')
        respData = resp.data[0]
        self.assertEqual('id' in respData, True)
        self.assertEqual('first_name' in respData, True)
        self.assertEqual('last_name' in respData, True)
        self.assertEqual('group' in respData, True)


class APITest_PersonGroups_last(APITestCase):
    """Class for testing PersonGroup - last items API requests"""

    def test_last_items(self):
        """Testing access to some last groups - primary use"""
        fixture = AutoFixture(PersonGroup)
        groupsGenerated = fixture.create(20)[-5:]
        resp = self.client.get(reverse('api:persongroup-list') + '?onlyLastItems=5')
        for (i, group) in enumerate(resp.data):
            # checking only id field.
            # If this is correct and other fields aren't, something wrong is happening in serializer
            self.assertEqual(groupsGenerated[i].id, group['id'])

    def test_empty_database(self):
        """Testing access to last groups, when database is empty"""
        resp = self.client.get(reverse('api:persongroup-list') + '?onlyLastItems=5')
        self.assertEqual(resp.data, [])

    def test_not_enough(self):
        """Testing last groups, when in database isn't enough data"""
        fixture = AutoFixture(PersonGroup, generate_fk=True)
        groupsGenerated = fixture.create(5)
        resp = self.client.get(reverse('api:persongroup-list') + '?onlyLastItems=20')
        self.assertEqual(len(resp.data), len(groupsGenerated))


class WEBTests(StaticLiveServerTestCase):
    """ Here are all tests with real browser. Using nightwatch - see tests directory to properly set environment

    Strange things happen in here:
    - in test_personDataChangeForm, first created person has id=2
    - in many places get(id=<>) don't work: strange ID's in database
    It looks like AutoFixture.create() have problem in here (really? why?)
    Uncomment test_test01, test_test02, test_test03 to see the problem.

    When class inherits from StaticLiveServerTestCase:
Testing started at 21:46 ...
Creating test database for alias 'default'...
Generated in test01:
ID: 1 name: Quo perspiciati
ID: 2 name: Possimus libero evenie
ID: 3 name: Autem nostrum e
ID: 4 name: Unde dolorem simi
ID: 5 name: Omnis quidem esse
Generated in test02:
ID: 6 name: At ipsum explicabo
ID: 7 name: Ip
ID: 8 name: Ipsum culpa laudantium do
ID: 9 name: Officiis vero expedit
ID: 10 name: Cum dolorum
Generated in test03:
ID: 11 name: Omnis qu
ID: 12 name: Volupta
ID: 13 name: Itaque
ID: 14 name: Ex
ID: 15 name: Nam in p
Destroying test database for alias 'default'...

Process finished with exit code 0

    When class inherits from TestCase:
Testing started at 21:45 ...
Creating test database for alias 'default'...
Generated in test01:
ID: 1 name: Minus suscipit voluptatem
ID: 2 name: Animi quibusdam velit be
ID: 3 name: Ea
ID: 4 name: Quasi enim fugit
ID: 5 name: Eveniet temp
Generated in test02:
ID: 1 name: Consecte
ID: 2 name: Adipis
ID: 3 name: Aut sapiente
ID: 4 name: Odio ipsa veritatis quasi
ID: 5 name: Te
Generated in test03:
ID: 1 name: Nostrum err
ID: 2 name: Nihil enim nemo repudian
ID: 3 name: Expedita
ID: 4 name: Eius saepe
ID: 5 name: Ea repellendus dolores
Destroying test database for alias 'default'...

Process finished with exit code 0
    """

    # def test_test01(self):
    #     fixture = AutoFixture(PersonGroup)
    #     fixture.create(5)
    #     print('Generated in test01:')
    #     for g in PersonGroup.objects.all():
    #         print('ID:', str(g.id), 'name:', str(g))
    #
    # def test_test02(self):
    #     fixture = AutoFixture(PersonGroup)
    #     fixture.create(5)
    #     print('Generated in test02:')
    #     for g in PersonGroup.objects.all():
    #         print('ID:', str(g.id), 'name:', str(g))
    #
    # def test_test03(self):
    #     fixture = AutoFixture(PersonGroup)
    #     fixture.create(5)
    #     print('Generated in test03:')
    #     for g in PersonGroup.objects.all():
    #         print('ID:', str(g.id), 'name:', str(g))

    def test_001_pgroupAddForm(self):
        call('cd users/tests && nightwatch --test forms/pgroupAddForm.js', shell=True)
        # strange: get(id=1) isn't working
        group = PersonGroup.objects.all()[0]
        self.assertEqual(group.name, 'Group name')
        self.assertEqual(group.description, 'This is some group description')

    def test_002_personAddForm(self):
        fixture = AutoFixture(PersonGroup)
        fixture.create(1)
        group = PersonGroup.objects.all()[0]
        call('cd users/tests && nightwatch --test forms/personAddForm.js', shell=True)
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
        call('cd users/tests && nightwatch --test forms/personDataChange.js', shell=True)
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
        call('cd users/tests && nightwatch --test forms/personCardNumberChange.js', shell=True)
        person = Person.objects.all()[0]
        self.assertEqual(person.card_number, '2222222222')

    def test_005_userAddForm(self):
        # calling browser
        call('cd users/tests && nightwatch --test forms/userAddForm.js', shell=True)
        user = SysUser.objects.all()[0]
        self.assertEqual(user.username, 'username')
        self.assertEqual(user.first_name, 'First name')
        self.assertEqual(user.last_name, 'Last name')
        self.assertEqual(user.rank, 'kpr.')
        self.assertEqual(user.email, 'user@user.com')


class PEP8Test(TestCase):
    """All PEP8 tests"""
    def test_pep8(self):
        """Testing PEP8"""
        pep8style = pep8.StyleGuide(quiet=False, ignore=['E501'])
        result = pep8style.check_files(['users/admin.py', 'users/apiSerializers.py', 'users/models.py',
                                        'users/tests.py', 'users/views.py', 'users/filters.py'])
        self.assertEqual(result.total_errors, 0, 'Errors or warnings in PEP8 test')
