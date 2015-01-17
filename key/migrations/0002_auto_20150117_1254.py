# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('key', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='keyrule',
            name='person',
            field=models.ForeignKey(to='users.Person'),
            preserve_default=True,
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
        migrations.AddField(
            model_name='key',
            name='manager',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
