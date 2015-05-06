# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class AddACSRequestrTest(TestCase):
    """Basic ACS request add form tests: basically template views """

    def test_access(self):
        """ Testing access to template view """
        resp = self.client.get(reverse('add_ACSRequest'))
        self.assertEqual(resp.status_code, 200)
