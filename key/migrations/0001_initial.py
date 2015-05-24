# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('manager', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('persons', models.ManyToManyField(to='users.Person')),
            ],
            options={
                'verbose_name_plural': 'Strefy systemu',
                'verbose_name': 'Strefa systemu Keyowego',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KeyConfirm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('grant_privilege', models.BooleanField(default=False)),
                ('executed', models.BooleanField(default=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('grant_privilege', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('confirmed', models.BooleanField(default=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('key', models.ForeignKey(to='key.Key')),
                ('person', models.ForeignKey(to='users.Person')),
            ],
            options={
                'verbose_name_plural': 'Uprawnienia',
                'verbose_name': 'Uprawnienie',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='keyrequest',
            name='rule',
            field=models.ForeignKey(to='key.KeyRule'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='keyrequest',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='keyorder',
            name='rule',
            field=models.ForeignKey(to='key.KeyRule'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='keyorder',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='keyconfirm',
            name='order',
            field=models.ForeignKey(to='key.KeyOrder'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='keyconfirm',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
