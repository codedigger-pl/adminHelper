# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils import timezone

from autofixture import AutoFixture

from users.models import PersonGroup


class PersonGroupClassTest(TestCase):
    """Base PersonGroup class tests"""

    def test_get_creation_date_properties(self):
        """ Testing correct date and time returning from creation_date field
        :return:
        """
        fixture = AutoFixture(PersonGroup)
        group = fixture.create(1)[0]
        someDate = timezone.now()
        group.creation_date = someDate
        group.save()
        self.assertEqual(someDate.date(), group.creation_date_date)
        self.assertEqual(someDate.time(), group.creation_date_time)
