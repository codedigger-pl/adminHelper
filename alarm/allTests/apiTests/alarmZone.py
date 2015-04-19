# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from autofixture import AutoFixture

from random import randint

from alarm.models import AlarmZone, AlarmRule
from users.models import SysUser


class APIAlarmZoneTest(APITestCase):
    """All primary API tests"""

    def test_access_alarmzones(self):
        """Testing access to alarm zone list"""
        resp = self.client.get(reverse('api:alarmzone-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_alarmzones_access(self):
        """Testing access to random created alarm zones objects"""
        fixture = AutoFixture(AlarmZone, generate_fk=True)
        zones = fixture.create(20)
        for z in zones:
            resp = self.client.get(reverse('api:alarmzone-detail', kwargs={'pk': z.id}))
            self.assertEqual(status.HTTP_200_OK, resp.status_code)

    def _test_persons_count(self):
        """Testing retrieving persons count"""
        count = randint(3,20)
        person_fixture = AutoFixture(SysUser, generate_fk=True)
        persons = person_fixture.create(count)

        zone_fixture = AutoFixture(AlarmZone)
        zone = zone_fixture.create(1)[0]

        rule_fixture = AutoFixture(AlarmRule)
        rules = rule_fixture.create(count)

        for i in range(count):
            rule = rules[i]
            rule.person = persons[i]
            rule.save()

        resp = self.client.get(reverse('api:alarmzone-persons-count', kwargs={'pk': zone.id}))
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        self.assertEqual(count, resp.data['count'])
