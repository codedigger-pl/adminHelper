# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils import timezone
from autofixture import AutoFixture

from alarm.models import AlarmZone


class AlarmZoneTest(TestCase):
    """Testing AlarmZone class"""

    def test_get_creation_date_properties(self):
        """ Testing correct date and time returning from creation_date field
        :return:
        """
        fixture = AutoFixture(AlarmZone, generate_fk=True)
        zone = fixture.create(1)[0]
        someDate = timezone.now()
        zone.creation_date = someDate
        zone.save()
        self.assertEqual(someDate.date(), zone.creation_date_date)
        self.assertEqual(someDate.time(), zone.creation_date_time)