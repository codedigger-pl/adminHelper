# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from autofixture import AutoFixture

from random import randint

from key.models import Key, KeyRule
from users.models import SysUser


class APIKeyZoneTest(APITestCase):
    """All primary API tests"""

    def test_access_keys(self):
        """Testing access to Key zone list"""
        resp = self.client.get(reverse('api:key-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_keys_access(self):
        """Testing access to random created Key zones objects"""
        fixture = AutoFixture(Key, generate_fk=True)
        keys = fixture.create(20)
        for k in keys:
            resp = self.client.get(reverse('api:key-detail', kwargs={'pk': k.id}))
            self.assertEqual(status.HTTP_200_OK, resp.status_code)

    def _test_persons_count(self):
        """Testing retrieving persons count"""
        count = randint(3,20)
        person_fixture = AutoFixture(SysUser, generate_fk=True)
        persons = person_fixture.create(count)

        key_fixture = AutoFixture(Key)
        key = key_fixture.create(1)[0]

        rule_fixture = AutoFixture(KeyRule)
        rules = rule_fixture.create(count)

        for i in range(count):
            rule = rules[i]
            rule.person = persons[i]
            rule.save()

        resp = self.client.get(reverse('api:key-persons-count', kwargs={'pk': key.id}))
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        self.assertEqual(count, resp.data['count'])
