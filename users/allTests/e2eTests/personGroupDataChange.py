# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call
from autofixture import AutoFixture

from users.models import PersonGroup
from .userLogin import create_test_user


class PersonGroupDataChangeTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_pgroupAddForm(self):
        create_test_user()
        fixture = AutoFixture(PersonGroup)
        fixture.create(1)
        self.assertEqual(0,
                         call('nightwatch --test users/allTests/e2eTests/personGroupDataChange.js', shell=True),
                         'Nighwatch tests failed')
        group = PersonGroup.objects.all()[0]
        self.assertEqual(group.name, 'New group name')
        self.assertEqual(group.description, 'New group description')
