# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils import timezone

from autofixture import AutoFixture

from users.models import Person


class PersonClassTest(TestCase):
    """ All test for class Person.
    """
    def test_last_name_uppercase(self):
        fixture = AutoFixture(Person, generate_fk=True)
        fixture.create(1)
        person = Person.objects.get(id=1)
        self.assertEqual(str(person.last_name).isupper(), True)

    def test_get_creation_date_properties(self):
        """ Testing correct date and time returning from creation_date field
        :return:
        """
        fixture = AutoFixture(Person, generate_fk=True)
        fixture.create(1)
        person = Person.objects.get(id=1)
        someDate = timezone.now()
        person.creation_date = someDate
        person.save()
        self.assertEqual(someDate.date(), person.creation_date_date)
        self.assertEqual(someDate.time(), person.creation_date_time)