# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from rest_framework.test import APITestCase
from rest_framework import status
from autofixture import AutoFixture

from random import randint

from users.models import PersonGroup, Person, SysUser


class APIPersonGroupTest(APITestCase):
    """All primary API tests"""

    def setUp(self):
        super(APIPersonGroupTest, self).setUp()
        user = SysUser()
        user.username = 'test_user'
        user.set_password('test_user')
        user.save()
        self.client.post(reverse('api:sysuser-login'), {'username': 'test_user', 'password': 'test_user'})


    def test_access_personGroups(self):
        """Testing access to persons API values"""
        resp = self.client.get(reverse('api:persongroup-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_personGroups_access(self):
        """Testing access to random created PersonGroup objects"""
        fixture = AutoFixture(PersonGroup)
        groups = fixture.create(20)
        for g in groups:
            resp = self.client.get(reverse('api:persongroup-detail', kwargs={'pk': g.id}))
            self.assertEqual(status.HTTP_200_OK, resp.status_code)

    def test_count(self):
        """Testing elements count"""
        count = randint(1, 20)
        fixture = AutoFixture(PersonGroup)
        fixture.create(count)
        resp = self.client.get(reverse('api:persongroup-count'))
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        self.assertEqual(count, resp.data['count'])

    def test_last_registered(self):
        """Testing retrieve last registered group"""
        fixture = AutoFixture(PersonGroup)
        last_registered = fixture.create(20)[-1]
        resp = self.client.get(reverse('api:persongroup-last-registered'))
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        self.assertEqual(last_registered.name, resp.data['name'])

    def test_person_count(self):
        """Testing person count"""
        group_fixture = AutoFixture(PersonGroup)
        group = group_fixture.create(1)[0]

        count = randint(3, 30)
        person_fixture = AutoFixture(Person)
        persons = person_fixture.create(count)
        for person in persons:
            person.group = group
            person.save()

        resp = self.client.get(reverse('api:persongroup-person-count', kwargs={'pk': group.id}))
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        self.assertEqual(count, resp.data['count'])


class APIPersonGroup_lastItems(APITestCase):
    """Testing last items from API"""
    def setUp(self):
        super(APIPersonGroup_lastItems, self).setUp()
        user = SysUser()
        user.username = 'test_user'
        user.set_password('test_user')
        user.save()
        self.client.post(reverse('api:sysuser-login'), {'username': 'test_user', 'password': 'test_user'})

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
