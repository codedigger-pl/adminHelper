# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class AddAlarmRequestrTest(TestCase):
    """Basic alarm request add form tests: basically template views """

    def test_access(self):
        """ Testing access to template view """
        resp = self.client.get(reverse('add_alarmRequest'))
        self.assertEqual(resp.status_code, 200)
