# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils import timezone
from autofixture import AutoFixture

from acs.models import ACSRequest


class ACSRequestTest(TestCase):
    """Testing ACSRequest class"""

    def test_get_creation_date_properties(self):
        """ Testing correct date and time returning from creation_date field
        :return:
        """
        fixture = AutoFixture(ACSRequest, generate_fk=True)
        request = fixture.create(1)[0]
        someDate = timezone.now()
        request.creation_date = someDate
        request.save()
        self.assertEqual(someDate.date(), request.creation_date_date)
        self.assertEqual(someDate.time(), request.creation_date_time)