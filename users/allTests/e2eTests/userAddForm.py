# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call

from users.models import SysUser


class UserAddFormTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_userAddForm(self):
        # calling browser
        call('cd users/allTests/e2eTests && nightwatch --test userAddForm.js', shell=True)
        user = SysUser.objects.all()[0]
        self.assertEqual(user.username, 'username')
        self.assertEqual(user.first_name, 'First name')
        self.assertEqual(user.last_name, 'Last name')
        self.assertEqual(user.rank, 'kpr.')
        self.assertEqual(user.email, 'user@user.com')