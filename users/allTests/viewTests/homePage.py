# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class HomePageTest(TestCase):
    """Basic Home Page tests"""

    def test_access(self):
        """ Testing access to home page """
        resp = self.client.get(reverse('homepage'))
        self.assertEqual(resp.status_code, 200)
