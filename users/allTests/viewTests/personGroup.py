# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class PersonGroupTest(TestCase):
    """Basic person groups test: basically template views """

    def test_access_detail(self):
        """ Testing access to detail template view """
        resp = self.client.get(reverse('pgroup_detail'))
        self.assertEqual(resp.status_code, 200)

    def test_access_list(self):
        """ Testing access to list template view """
        resp = self.client.get(reverse('pgroup_list'))
        self.assertEqual(resp.status_code, 200)
