# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class AlarmOverviewTest(TestCase):
    """Basic alarm overview tests: basically template views """

    def test_access(self):
        """ Testing access to detail template view """
        resp = self.client.get(reverse('alarmOverview'))
        self.assertEqual(resp.status_code, 200)
