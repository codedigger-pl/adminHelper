# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils import timezone
from autofixture import AutoFixture

from key.models import KeyOrder


class KeyOrderTest(TestCase):
    """Testing ACSZone class"""

    def test_get_creation_date_properties(self):
        """ Testing correct date and time returning from creation_date field
        :return:
        """
        fixture = AutoFixture(KeyOrder, generate_fk=True)
        order = fixture.create(1)[0]
        someDate = timezone.now()
        order.creation_date = someDate
        order.save()
        self.assertEqual(someDate.date(), order.creation_date_date)
        self.assertEqual(someDate.time(), order.creation_date_time)