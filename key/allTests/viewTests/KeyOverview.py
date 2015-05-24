# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class KeyOverviewTest(TestCase):
    """Basic ACS overview tests: basically template views """

    def test_access(self):
        """ Testing access to detail template view """
        resp = self.client.get(reverse('keyOverview'))
        self.assertEqual(resp.status_code, 200)
