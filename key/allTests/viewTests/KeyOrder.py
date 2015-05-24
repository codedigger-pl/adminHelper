# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class AddKeyOrderTest(TestCase):
    """Basic ACS order add form tests: basically template views """

    def test_access(self):
        """ Testing access to template view """
        resp = self.client.get(reverse('add_keyOrder'))
        self.assertEqual(resp.status_code, 200)
