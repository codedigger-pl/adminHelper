# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call

from users.models import PersonGroup, Person, SysUser


class PersonGroupAddFormTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_pgroupAddForm(self):
        self.assertEqual(0,
                         call('cd users/allTests/e2eTests && nightwatch --test pgroupAddForm.js', shell=True),
                         'Nighwatch tests failed')
        group = PersonGroup.objects.all()[0]
        self.assertEqual(group.name, 'Group name')
        self.assertEqual(group.description, 'This is some group description')
