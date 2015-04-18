# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from autofixture import AutoFixture

from random import randint

from alarm.models import AlarmZone


class APIAlarmZoneTest(APITestCase):
    """All primary API tests"""

    def test_access_alarmzones(self):
        """Testing access to persons API values"""
        resp = self.client.get(reverse('api:alarmzone-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_alarmzones_access(self):
        """Testing access to random created alarm zones objects"""
        fixture = AutoFixture(AlarmZone, generate_fk=True)
        zones = fixture.create(20)
        for z in zones:
            resp = self.client.get(reverse('api:alarmzone-detail', kwargs={'pk': z.id}))
            self.assertEqual(status.HTTP_200_OK, resp.status_code)
