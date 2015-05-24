# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from autofixture import AutoFixture

from random import randint

from key.models import KeyRequest


class APIKeyRequestTest(APITestCase):
    """All primary API tests"""

    def test_access_KeyRequest(self):
        """Testing access to key request list"""
        resp = self.client.get(reverse('api:keyrequest-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_keyRequests_access(self):
        """Testing access to random created key requests objects"""
        fixture = AutoFixture(KeyRequest, generate_fk=True)
        requests = fixture.create(20)
        for r in requests:
            resp = self.client.get(reverse('api:keyrequest-detail', kwargs={'pk': r.id}))
            self.assertEqual(status.HTTP_200_OK, resp.status_code)
