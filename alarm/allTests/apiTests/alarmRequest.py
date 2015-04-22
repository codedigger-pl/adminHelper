# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from autofixture import AutoFixture

from random import randint

from alarm.models import AlarmRequest


class APIAlarmRequestTest(APITestCase):
    """All primary API tests"""

    def test_access_alarmrequest(self):
        """Testing access to alarm request list"""
        resp = self.client.get(reverse('api:alarmrequest-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_alarmrequests_access(self):
        """Testing access to random created alarm requests objects"""
        fixture = AutoFixture(AlarmRequest, generate_fk=True)
        requests = fixture.create(20)
        for r in requests:
            resp = self.client.get(reverse('api:alarmrequest-detail', kwargs={'pk': r.id}))
            self.assertEqual(status.HTTP_200_OK, resp.status_code)
