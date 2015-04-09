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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Klucze',
                'verbose_name': 'Klucz',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KeyConfirm',
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
            name='KeyOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('addRule', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Polecenia zmiany uprawnień',
                'verbose_name': 'Polecenie zmiany uprawnień',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KeyRequest',
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
            name='KeyRule',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('confirmed', models.BooleanField(default=False)),
                ('key', models.ForeignKey(to='key.Key')),
            ],
            options={
                'verbose_name_plural': 'Uprawnienia',
                'verbose_name': 'Uprawnienie',
            },
            bases=(models.Model,),
        ),
    ]
