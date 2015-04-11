# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from autofixture import AutoFixture

from random import randint

from users.models import PersonGroup


class APIPersonGroupTest(APITestCase):
    """All primary API tests"""

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


class APIPersonGroup_lastItems(APITestCase):
    """Testing last items from API"""

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
