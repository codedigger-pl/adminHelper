# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from autofixture import AutoFixture

from random import randint

from acs.models import ACSRequest


class APIACSRequestTest(APITestCase):
    """All primary API tests"""

    def test_access_ACSrequest(self):
        """Testing access to ACS request list"""
        resp = self.client.get(reverse('api:acsrequest-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_ACSrequests_access(self):
        """Testing access to random created ACS requests objects"""
        fixture = AutoFixture(ACSRequest, generate_fk=True)
        requests = fixture.create(20)
        for r in requests:
            resp = self.client.get(reverse('api:acsrequest-detail', kwargs={'pk': r.id}))
            self.assertEqual(status.HTTP_200_OK, resp.status_code)
