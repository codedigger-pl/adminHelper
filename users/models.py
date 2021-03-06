# -*- coding: utf-8 -*-

from django.conf import settings
from django.dispatch import receiver
from django.db import models
from django.db.models import ForeignKey, CharField, BooleanField, TextField, DateTimeField, ImageField
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

from rest_framework.authtoken.models import Token


class PersonGroup(models.Model):
    """ Class PersonGroup

    Describes all information about person groups
    """
    # group name
    name = CharField(max_length=25,
                     unique=True)
    # group description
    description = TextField(blank=True)

    # ---== read only fields ==---
    # group creation date
    creation_date = DateTimeField(auto_now_add=True)
    creation_date_date = property(lambda self: self.creation_date.date())
    creation_date_time = property(lambda self: self.creation_date.time())

    class Meta:
        verbose_name = 'Grupa osób'
        verbose_name_plural = 'Grupy osób'

    def __str__(self):
        return self.name


# Military ranks
# in Polish, it is hard to translate this
RANK_PAN = 'pan'
RANK_PANI = 'pani'
RANK_SZEREGOWY = 'szer.'
RANK_ST_SZEREGOWY = 'st. szer.'
RANK_KAPRAL = 'kpr.'
RANK_ST_KAPRAL = 'st. kpr.'
RANK_PLUTONOWY = 'plut.'
RANK_SIERZANT = 'sierż'
RANK_ST_SIERZANT = 'st. sierż.'
RANK_ML_CHORAZY = 'mł. chor.'
RANK_CHORAZY = 'chor.'
RANK_ST_CHORAZY = 'st. chor.'
RANK_ST_CHORAZY_SZTAB = 'st. chor. sztab.'
RANK_PODPORUCZNIK = 'ppor.'
RANK_PORUCZNIK = 'por'
RANK_KAPITAN = 'kpt.'
RANK_MAJOR = 'mjr'
RANK_PODPULKOWNIK = 'ppłk'
RANK_PULKOWNIK = 'płk'
RANK_GEN_BRYGADY = 'gen. bryg.'
RANK_GEN_DYWIZJI = 'gen. dyw.'
RANK_GEN_BRONI = 'gen. broni'
RANK_GENERAL = 'gen.'

RANK_CHOICES = (
    (RANK_PAN, 'pan'),
    (RANK_PANI, 'pani'),
    (RANK_SZEREGOWY, 'szeregowy'),
    (RANK_ST_SZEREGOWY, 'starszy szeregowy'),
    (RANK_KAPRAL, 'kapral'),
    (RANK_ST_KAPRAL, 'starszy kapral'),
    (RANK_PLUTONOWY, 'plutonowy'),
    (RANK_SIERZANT, 'sierżant'),
    (RANK_ST_SIERZANT, 'starszy sierżant'),
    (RANK_ML_CHORAZY, 'młodszt chorąży'),
    (RANK_CHORAZY, 'chorąży'),
    (RANK_ST_CHORAZY, 'starszy chorąży'),
    (RANK_ST_CHORAZY_SZTAB, 'starszy chorąży sztabowy'),
    (RANK_PODPORUCZNIK, 'podporucznik'),
    (RANK_PORUCZNIK, 'porucznik'),
    (RANK_KAPITAN, 'kapitan'),
    (RANK_PODPULKOWNIK, 'podpułkownik'),
    (RANK_PULKOWNIK, 'pułkownik'),
    (RANK_GEN_BRYGADY, 'generał brygady'),
    (RANK_GEN_DYWIZJI, 'generał dywizji'),
    (RANK_GEN_BRONI, 'generał broni'),
    (RANK_GENERAL, 'generał'),
)


class Person(models.Model):
    """ Class Person

    Describes all information about person in any system
    """
    # person first name
    first_name = CharField(max_length=25)
    # person last name
    last_name = CharField(max_length=25)
    # person is active?
    is_active = BooleanField(default=True)
    # person access system card number
    card_number = CharField(max_length=15, blank=True)
    # person rank (pan/pani/kpt./mjr/por. etc)
    rank = CharField(max_length=20, choices=RANK_CHOICES)
    # person group
    group = ForeignKey('PersonGroup')
    # person photo
    photo = ImageField(upload_to='photos/', blank=True, default=settings.STATIC_URL + 'img/unknown_user.jpg', null=True)

    # ---== read only fields ==---
    # person creation date
    creation_date = DateTimeField(auto_now_add=True)
    creation_date_date = property(lambda self: self.creation_date.date())
    creation_date_time = property(lambda self: self.creation_date.time())

    class Meta:
        verbose_name = 'Osoba'
        verbose_name_plural = 'Osoby'

        unique_together = (('first_name', 'last_name'))

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        """ save

        Saving Person information to database with:
        - changed last_name to uppercase

        :param args: args params
        :param kwargs: kwargs params
        :return:
        """
        self.last_name = str(self.last_name).upper()
        super(Person, self).save(*args, **kwargs)


class SysUser(AbstractUser):
    """ Class SysUser

    Django User class
    """
    # user rank (pan/pani/kpt./mjr/por. etc
    rank = CharField(max_length=20, choices=RANK_CHOICES, blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
#
#
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
