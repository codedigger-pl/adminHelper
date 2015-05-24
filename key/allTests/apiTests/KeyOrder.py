# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from autofixture import AutoFixture

from random import randint
from time import sleep

from key.models import KeyOrder, KeyRule, Key
from users.models import Person


class APIKeyOrderTest(APITestCase):
    """All primary API tests"""

    def test_access_keyOrder(self):
        """Testing access to Key order list"""
        resp = self.client.get(reverse('api:keyorder-list'))
        self.assertEqual(resp.status_code, 200)

    def test_random_keyOrder_access(self):
        """Testing access to random created Key order objects"""
        fixture = AutoFixture(KeyOrder, generate_fk=True)
        orders = fixture.create(20)
        for o in orders:
            resp = self.client.get(reverse('api:keyorder-detail', kwargs={'pk': o.id}))
            self.assertEqual(status.HTTP_200_OK, resp.status_code)

    def test_param_nonExecutedOnly(self):
        """Testing list of executed and non-executed orders"""
        # with empty database
        non_exec_response = self.client.get(reverse('api:keyorder-list')+'?nonExecutedOnly')
        self.assertEqual(status.HTTP_200_OK, non_exec_response.status_code)
        self.assertEqual(0, len(non_exec_response.data))

        # adding some orders
        fixture = AutoFixture(KeyOrder, generate_fk=True)
        orders = fixture.create(20)

        # none order is executed
        non_exec_response = self.client.get(reverse('api:keyorder-list')+'?nonExecutedOnly')
        response = self.client.get(reverse('api:keyorder-list'))
        self.assertEqual(status.HTTP_200_OK, non_exec_response.status_code)
        self.assertEqual(20, len(non_exec_response.data))
        self.assertEqual(len(response.data), len(non_exec_response.data))

        # executing all orders
        for order in orders:
            order.executed = True
            order.save()

        # all orders are executed
        non_exec_response = self.client.get(reverse('api:keyorder-list')+'?nonExecutedOnly')
        response = self.client.get(reverse('api:keyorder-list'))
        self.assertEqual(status.HTTP_200_OK, non_exec_response.status_code)
        self.assertEqual(0, len(non_exec_response.data))
        self.assertEqual(20, len(response.data))

        # adding one non-executed order
        fixture.create(1)
        non_exec_response = self.client.get(reverse('api:keyorder-list')+'?nonExecutedOnly')
        response = self.client.get(reverse('api:keyorder-list'))
        self.assertEqual(status.HTTP_200_OK, non_exec_response.status_code)
        self.assertEqual(1, len(non_exec_response.data))
        self.assertEqual(21, len(response.data))

    def test_execute_order(self):
        """Testing order execute"""
        fixture = AutoFixture(Person, generate_fk=True)
        persons = fixture.create(10)

        fixture = AutoFixture(Key, generate_fk=True)
        key = fixture.create(1)[0]
        key.persons.clear()
        key.save()

        fixture = AutoFixture(KeyRule, generate_fk=True)
        rules = fixture.create(10)
        for person, rule in zip(persons, rules):
            rule.person = person
            rule.key = key
            rule.save()

        fixture = AutoFixture(KeyOrder, generate_fk=True)
        orders = fixture.create(10)

        for order, rule in zip(orders, rules):
            order.rule = rule
            order.grant_privilege = True
            order.save()

        self.assertEqual(0, key.persons.count())

        for order in orders:
            self.assertFalse(order.executed)

        for order in orders:
            resp = self.client.post(reverse('api:keyorder-execute', kwargs={'pk': order.id}), {})
            self.assertEqual(status.HTTP_200_OK, resp.status_code)

        orders = KeyOrder.objects.all()
        for order in orders:
            self.assertTrue(order.executed)

        key = Key.objects.get(id=key.id)
        self.assertEqual(10, key.persons.count())
