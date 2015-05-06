# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from autofixture import AutoFixture

from random import randint

from acs.models import ACSRule


class APIACSRuleTest(APITestCase):
    """All primary API tests"""

    def test_access_ACSrules(self):
        """Testing access to persons API values"""
        resp = self.client.get(reverse('api:acsrule-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_ACSrules_access(self):
        """Testing access to random created ACS zones objects"""
        fixture = AutoFixture(ACSRule, generate_fk=True)
        rules = fixture.create(20)
        for r in rules:
            resp = self.client.get(reverse('api:acsrule-detail', kwargs={'pk': r.id}))
            self.assertEqual(status.HTTP_200_OK, resp.status_code)
