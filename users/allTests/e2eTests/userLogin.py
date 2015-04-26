# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from subprocess import call

from users.models import SysUser


def create_test_user():
    user = SysUser()
    user.username = 'test_user'
    user.set_password('test_user')
    user.save()

class UserLoginTest(StaticLiveServerTestCase):
    """All tests with nightwatch and Selenium server"""

    def test_userLogin(self):
        # calling browser
        create_test_user()
        self.assertEqual(0,
                         call('nightwatch --test users/allTests/e2eTests/userLogin.js', shell=True),
                         'Nighwatch tests failed')
