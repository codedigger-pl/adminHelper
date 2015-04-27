# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from autofixture import AutoFixture

from random import randint

from alarm.models import AlarmOrder


class APIAlarmOrderTest(APITestCase):
    """All primary API tests"""

    def test_access_alarmorder(self):
        """Testing access to alarm order list"""
        resp = self.client.get(reverse('api:alarmorder-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_alarmorder_access(self):
        """Testing access to random created alarm order objects"""
        fixture = AutoFixture(AlarmOrder, generate_fk=True)
        orders = fixture.create(20)
        for o in orders:
            resp = self.client.get(reverse('api:alarmorder-detail', kwargs={'pk': o.id}))
            self.assertEqual(status.HTTP_200_OK, resp.status_code)

    def test_param_nonExecutedOnly(self):
        """Testing list of executed and non-executed orders"""
        # with empty database
        non_exec_response = self.client.get(reverse('api:alarmorder-list')+'?nonExecutedOnly')
        self.assertEqual(status.HTTP_200_OK, non_exec_response.status_code)
        self.assertEqual(0, len(non_exec_response.data))

        # adding some orders
        fixture = AutoFixture(AlarmOrder, generate_fk=True)
        orders = fixture.create(20)

        # none order is executed
        non_exec_response = self.client.get(reverse('api:alarmorder-list')+'?nonExecutedOnly')
        response = self.client.get(reverse('api:alarmorder-list'))
        self.assertEqual(status.HTTP_200_OK, non_exec_response.status_code)
        self.assertEqual(20, len(non_exec_response.data))
        self.assertEqual(len(response.data), len(non_exec_response.data))

        # executing all orders
        for order in orders:
            order.executed = True
            order.save()

        # all orders are executed
        non_exec_response = self.client.get(reverse('api:alarmorder-list')+'?nonExecutedOnly')
        response = self.client.get(reverse('api:alarmorder-list'))
        self.assertEqual(status.HTTP_200_OK, non_exec_response.status_code)
        self.assertEqual(0, len(non_exec_response.data))
        self.assertEqual(20, len(response.data))

        # adding one non-executed order
        fixture.create(1)
        non_exec_response = self.client.get(reverse('api:alarmorder-list')+'?nonExecutedOnly')
        response = self.client.get(reverse('api:alarmorder-list'))
        self.assertEqual(status.HTTP_200_OK, non_exec_response.status_code)
        self.assertEqual(1, len(non_exec_response.data))
        self.assertEqual(21, len(response.data))

