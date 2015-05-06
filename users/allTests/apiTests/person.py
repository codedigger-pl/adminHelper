# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from autofixture import AutoFixture
from random import randint

from alarm.models import AlarmZone
from acs.models import ACSZone
from users.models import Person, SysUser


class APIPersonTest(APITestCase):
    """All primary API tests"""

    def setUp(self):
        super(APIPersonTest, self).setUp()
        user = SysUser()
        user.username = 'test_user'
        user.set_password('test_user')
        user.save()
        self.client.post(reverse('api:sysuser-login'), {'username': 'test_user', 'password': 'test_user'})

    def test_access_persons(self):
        """Testing access to persons API values"""
        resp = self.client.get(reverse('api:person-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_persons_access(self):
        """Testing access to random created Person objects"""
        fixture = AutoFixture(Person, generate_fk=True)
        persons = fixture.create(20)
        for p in persons:
            resp = self.client.get(reverse('api:person-detail', kwargs={'pk': p.id}))
            self.assertEqual(status.HTTP_200_OK, resp.status_code)

    def test_count(self):
        """Testing elements count"""
        count = randint(1, 20)
        fixture = AutoFixture(Person, generate_fk=True)
        fixture.create(count)
        resp = self.client.get(reverse('api:person-count'))
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        self.assertEqual(count, resp.data['count'])

    def test_last_registered(self):
        """Testing last registered person"""
        fixture = AutoFixture(Person, generate_fk=True)
        last_registered = fixture.create(20)[-1]
        resp = self.client.get(reverse('api:person-last-registered'))
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        self.assertEqual(last_registered.last_name + ' ' + last_registered.first_name, resp.data['name'])

    def test_alarm_zone_list(self):
        """Testing alarm zone lists, where some user has access"""
        fixture = AutoFixture(Person, generate_fk=True)
        person = fixture.create(1)[0]

        resp = self.client.get(reverse('api:person-alarm-zones', kwargs={'pk': person.id}))
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        self.assertEqual(0, len(resp.data))

        fixture = AutoFixture(AlarmZone, generate_fk=True)
        zones = fixture.create(10)
        for zone in zones:
            zone.persons.add(person)
            zone.save()

        resp = self.client.get(reverse('api:person-alarm-zones', kwargs={'pk': person.id}))
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        self.assertEqual(10, len(resp.data))

    def test_ACS_zone_list(self):
        """Testing ACS zone lists, where some user has access"""
        fixture = AutoFixture(Person, generate_fk=True)
        person = fixture.create(1)[0]

        resp = self.client.get(reverse('api:person-acs-zones', kwargs={'pk': person.id}))
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        self.assertEqual(0, len(resp.data))

        fixture = AutoFixture(ACSZone, generate_fk=True)
        zones = fixture.create(10)
        for zone in zones:
            zone.persons.add(person)
            zone.save()

        resp = self.client.get(reverse('api:person-acs-zones', kwargs={'pk': person.id}))
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        self.assertEqual(10, len(resp.data))


class APIPersonsTest_lastItems(APITestCase):
    """Testing last items from API"""

    def setUp(self):
        super(APIPersonsTest_lastItems, self).setUp()
        user = SysUser()
        user.username = 'test_user'
        user.set_password('test_user')
        user.save()
        self.client.post(reverse('api:sysuser-login'), {'username': 'test_user', 'password': 'test_user'})

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

    def setUp(self):
        super(APITest_Person_serializerSwitcher, self).setUp()
        user = SysUser()
        user.username = 'test_user'
        user.set_password('test_user')
        user.save()
        self.client.post(reverse('api:sysuser-login'), {'username': 'test_user', 'password': 'test_user'})

    def test_minimal_serializer(self):
        """Checking, if minimal information are present"""
        fixture = AutoFixture(Person, generate_fk=True)
        fixture.create(5)
        resp = self.client.get(reverse('api:person-list') + '?modelType=minimal')
        respData = resp.data[0]
        self.assertEqual('id' in respData, True)
        self.assertEqual('first_name' in respData, True)
        self.assertEqual('last_name' in respData, True)
        self.assertEqual('group' in respData, True)
