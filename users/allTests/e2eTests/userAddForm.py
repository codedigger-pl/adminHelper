# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call

from users.models import SysUser
from .userLogin import create_test_user


class UserAddFormTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_userAddForm(self):
        create_test_user()
        # calling browser
        self.assertEqual(0,
                         call('nightwatch --test users/allTests/e2eTests/userAddForm.js', shell=True),
                         'Nighwatch tests failed')
        user = SysUser.objects.last()
        self.assertEqual(user.username, 'username')
        self.assertEqual(user.first_name, 'First name')
        self.assertEqual(user.last_name, 'Last name')
        self.assertEqual(user.rank, 'kpr.')
        self.assertEqual(user.email, 'user@user.com')
