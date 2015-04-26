# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class FormsViewTest(TestCase):
    """Basic forms page tests"""

    def test_access_login(self):
        """Testing access to login form"""
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)
