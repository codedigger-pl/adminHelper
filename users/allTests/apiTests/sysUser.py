# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from autofixture import AutoFixture
from random import randint

from users.models import SysUser


class APISysUserTest(APITestCase):
    """All primary API tests"""

    def test_access_user(self):
        """Testing access to persons API values"""
        resp = self.client.get(reverse('api:sysuser-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_user_access(self):
        """Testing access to random created Person objects"""
        fixture = AutoFixture(SysUser, generate_fk=True)
        users = fixture.create(20)
        for u in users:
            resp = self.client.get(reverse('api:sysuser-detail', kwargs={'pk': u.id}))
            self.assertEqual(resp.status_code, 200)

    def test_changing_user_password(self):
        """Testing user password change functionality"""
        user, = AutoFixture(SysUser, generate_fk=True).create(1)
        old_password = user.password

        url = reverse('api:sysuser-set-password', kwargs={'pk': user.id})
        data = {'password': 'new_password'}
        client = APIClient()
        response = client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, 'Server returned ' + str(response.data))
        user = SysUser.objects.all()[0]
        self.assertNotEqual(old_password, user.password, 'Password not changed')

    def test_count(self):
        """Testing elements count"""
        count = randint(1, 20)
        fixture = AutoFixture(SysUser)
        fixture.create(count)
        resp = self.client.get(reverse('api:sysuser-count'))
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        self.assertEqual(count, resp.data['count'])
