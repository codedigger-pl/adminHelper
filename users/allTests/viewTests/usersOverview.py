# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class UsersOverviewTest(TestCase):
    """Basic users overview page tests ('/users/*') """

    def test_access_overview(self):
        """ Testing access to users overview page """
        resp = self.client.get(reverse('usersOverview'))
        self.assertEqual(resp.status_code, 200)