# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from autofixture import AutoFixture

from random import randint

from alarm.models import AlarmRule


class APIAlarmRuleTest(APITestCase):
    """All primary API tests"""

    def test_access_alarmrules(self):
        """Testing access to persons API values"""
        resp = self.client.get(reverse('api:alarmrule-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_alarmrules_access(self):
        """Testing access to random created alarm zones objects"""
        fixture = AutoFixture(AlarmRule, generate_fk=True)
        rules = fixture.create(20)
        for r in rules:
            resp = self.client.get(reverse('api:alarmrule-detail', kwargs={'pk': r.id}))
            self.assertEqual(status.HTTP_200_OK, resp.status_code)
