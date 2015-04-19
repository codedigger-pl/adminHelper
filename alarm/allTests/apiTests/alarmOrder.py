# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from autofixture import AutoFixture

from random import randint

from alarm.models import AlarmOrder


class APIAlarmOrderTest(APITestCase):
    """All primary API tests"""

    def test_access_alarmorder(self):
        """Testing access to alarm order list"""
        resp = self.client.get(reverse('api:alarmorder-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_alarmzones_access(self):
        """Testing access to random created alarm order objects"""
        fixture = AutoFixture(AlarmOrder, generate_fk=True)
        orders = fixture.create(20)
        for o in orders:
            resp = self.client.get(reverse('api:alarmorder-detail', kwargs={'pk': o.id}))
            self.assertEqual(status.HTTP_200_OK, resp.status_code)
