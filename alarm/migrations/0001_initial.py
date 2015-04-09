# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmConfirm',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('executionDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Potwierdzenia zmiany uprawnień',
                'verbose_name': 'Potwierdzenie zmiany uprawnień',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AlarmOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('addRule', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Polecenia zmiany uprawnień',
                'verbose_name': 'Polecenie zmiany uprawnień',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AlarmRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('addRule', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Prośby zmiany uprawnień',
                'verbose_name': 'Prośba zmiany uprawnień',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AlarmRule',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('confirmed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Uprawnienia',
                'verbose_name': 'Uprawnienie',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AlarmZone',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Strefy systemu',
                'verbose_name': 'Strefa systemu alarmowego',
            },
            bases=(models.Model,),
        ),
    ]
