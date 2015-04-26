# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call

from users.models import PersonGroup, Person, SysUser
from .userLogin import create_test_user


class PersonGroupAddFormTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_pgroupAddForm(self):
        create_test_user()
        self.assertEqual(0,
                         call('nightwatch --test users/allTests/e2eTests/pgroupAddForm.js', shell=True),
                         'Nighwatch tests failed')
        group = PersonGroup.objects.all()[0]
        self.assertEqual(group.name, 'Group name')
        self.assertEqual(group.description, 'This is some group description')
