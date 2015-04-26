# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class LoginTest(TestCase):
    """Basic forms page tests"""

    def test_access_login_form(self):
        """Testing access to login form"""
        resp = self.client.get(reverse('login_form'))
        self.assertEqual(resp.status_code, 200)

    def test_access_login_view(self):
        """Testing access to login page"""
        resp = self.client.get(reverse('login_view'))
        self.assertEqual(resp.status_code, 200)
