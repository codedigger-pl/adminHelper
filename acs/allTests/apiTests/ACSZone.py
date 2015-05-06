# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from autofixture import AutoFixture

from random import randint

from acs.models import ACSZone, ACSRule
from users.models import SysUser


class APIACSZoneTest(APITestCase):
    """All primary API tests"""

    def test_access_ACSzones(self):
        """Testing access to ACS zone list"""
        resp = self.client.get(reverse('api:acszone-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_ACSzones_access(self):
        """Testing access to random created ACS zones objects"""
        fixture = AutoFixture(ACSZone, generate_fk=True)
        zones = fixture.create(20)
        for z in zones:
            resp = self.client.get(reverse('api:acszone-detail', kwargs={'pk': z.id}))
            self.assertEqual(status.HTTP_200_OK, resp.status_code)

    def _test_persons_count(self):
        """Testing retrieving persons count"""
        count = randint(3,20)
        person_fixture = AutoFixture(SysUser, generate_fk=True)
        persons = person_fixture.create(count)

        zone_fixture = AutoFixture(ACSZone)
        zone = zone_fixture.create(1)[0]

        rule_fixture = AutoFixture(ACSRule)
        rules = rule_fixture.create(count)

        for i in range(count):
            rule = rules[i]
            rule.person = persons[i]
            rule.save()

        resp = self.client.get(reverse('api:acszone-persons-count', kwargs={'pk': zone.id}))
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        self.assertEqual(count, resp.data['count'])
