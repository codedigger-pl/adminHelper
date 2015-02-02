# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='cardNumber',
            new_name='card_number',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='lastName',
            new_name='last_name',
        ),
    ]
