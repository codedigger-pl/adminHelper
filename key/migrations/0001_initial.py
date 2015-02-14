# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Klucz',
                'verbose_name_plural': 'Klucze',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KeyConfirm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('executionDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Potwierdzenie zmiany uprawnień',
                'verbose_name_plural': 'Potwierdzenia zmiany uprawnień',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KeyOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('addRule', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Polecenie zmiany uprawnień',
                'verbose_name_plural': 'Polecenia zmiany uprawnień',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KeyRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('addRule', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Prośba zmiany uprawnień',
                'verbose_name_plural': 'Prośby zmiany uprawnień',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KeyRule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('key', models.ForeignKey(to='key.Key')),
            ],
            options={
                'verbose_name': 'Uprawnienie',
                'verbose_name_plural': 'Uprawnienia',
            },
            bases=(models.Model,),
        ),
    ]
