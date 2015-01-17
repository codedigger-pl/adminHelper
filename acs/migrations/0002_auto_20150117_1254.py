# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
        ('acs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acszone',
            name='manager',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acsrule',
            name='person',
            field=models.ForeignKey(to='users.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acsrule',
            name='zone',
            field=models.ForeignKey(to='acs.ACSZone'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acsrequest',
            name='rule',
            field=models.ForeignKey(to='acs.ACSRule'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acsrequest',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acsorder',
            name='rule',
            field=models.ForeignKey(to='acs.ACSRule'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acsorder',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acsconfirm',
            name='order',
            field=models.ForeignKey(to='acs.ACSOrder'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acsconfirm',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
