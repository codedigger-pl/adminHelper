# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ACSConfirm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('executionDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Potwierdzenie zmiany uprawnień',
                'verbose_name_plural': 'Potwierdzenia zmiany uprawnień',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ACSOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grant_privilege', models.BooleanField(default=False)),
                ('executed', models.BooleanField(default=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Polecenie zmiany uprawnień',
                'verbose_name_plural': 'Polecenia zmiany uprawnień',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ACSRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('grant_privilege', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Prośba zmiany uprawnień',
                'verbose_name_plural': 'Prośby zmiany uprawnień',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ACSRule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Uprawnienie',
                'verbose_name_plural': 'Uprawnienia',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ACSZone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Strefa systemu ACSowego',
                'verbose_name_plural': 'Strefy systemu',
            },
            bases=(models.Model,),
        ),
    ]
