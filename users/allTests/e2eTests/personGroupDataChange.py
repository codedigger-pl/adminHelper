# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from users.models import PersonGroup


class PersonGroupDataChangeTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_pgroupAddForm(self):
        fixture = AutoFixture(PersonGroup)
        fixture.create(1)
        self.assertEqual(0,
                         call('cd users/allTests/e2eTests && nightwatch --test personGroupDataChange.js', shell=True),
                         'Nighwatch tests failed')
        group = PersonGroup.objects.all()[0]
        self.assertEqual(group.name, 'New group name')
        self.assertEqual(group.description, 'New group description')
