# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
        ('alarm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarmzone',
            name='manager',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alarmrule',
            name='person',
            field=models.ForeignKey(to='users.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alarmrule',
            name='zone',
            field=models.ForeignKey(to='alarm.AlarmZone'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alarmrequest',
            name='rule',
            field=models.ForeignKey(to='alarm.AlarmRule'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alarmrequest',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alarmorder',
            name='rule',
            field=models.ForeignKey(to='alarm.AlarmRule'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alarmorder',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alarmconfirm',
            name='order',
            field=models.ForeignKey(to='alarm.AlarmOrder'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alarmconfirm',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
