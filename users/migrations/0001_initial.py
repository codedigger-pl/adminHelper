# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SysUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], max_length=30, verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=75, verbose_name='email address')),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rank', models.CharField(blank=True, max_length=20, choices=[('pan', 'pan'), ('pani', 'pani'), ('szer.', 'szeregowy'), ('st. szer.', 'starszy szeregowy'), ('kpr.', 'kapral'), ('st. kpr.', 'starszy kapral'), ('plut.', 'plutonowy'), ('sierż', 'sierżant'), ('st. sierż.', 'starszy sierżant'), ('mł. chor.', 'młodszt chorąży'), ('chor.', 'chorąży'), ('st. chor.', 'starszy chorąży'), ('st. chor. sztab.', 'starszy chorąży sztabowy'), ('ppor.', 'podporucznik'), ('por', 'porucznik'), ('kpt.', 'kapitan'), ('ppłk', 'podpułkownik'), ('płk', 'pułkownik'), ('gen. bryg.', 'generał brygady'), ('gen. dyw.', 'generał dywizji'), ('gen. broni', 'generał broni'), ('gen.', 'generał')])),
                ('groups', models.ManyToManyField(related_query_name='user', blank=True, to='auth.Group', related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', blank=True, to='auth.Permission', related_name='user_set', help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('is_active', models.BooleanField(default=True)),
                ('card_number', models.CharField(blank=True, max_length=15)),
                ('rank', models.CharField(max_length=20, choices=[('pan', 'pan'), ('pani', 'pani'), ('szer.', 'szeregowy'), ('st. szer.', 'starszy szeregowy'), ('kpr.', 'kapral'), ('st. kpr.', 'starszy kapral'), ('plut.', 'plutonowy'), ('sierż', 'sierżant'), ('st. sierż.', 'starszy sierżant'), ('mł. chor.', 'młodszt chorąży'), ('chor.', 'chorąży'), ('st. chor.', 'starszy chorąży'), ('st. chor. sztab.', 'starszy chorąży sztabowy'), ('ppor.', 'podporucznik'), ('por', 'porucznik'), ('kpt.', 'kapitan'), ('ppłk', 'podpułkownik'), ('płk', 'pułkownik'), ('gen. bryg.', 'generał brygady'), ('gen. dyw.', 'generał dywizji'), ('gen. broni', 'generał broni'), ('gen.', 'generał')])),
                ('photo', models.ImageField(blank=True, upload_to='photos/', default='/static/img/unknown_user.jpg', null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Osoby',
                'verbose_name': 'Osoba',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=25)),
                ('description', models.TextField(blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Grupy osób',
                'verbose_name': 'Grupa osób',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='group',
            field=models.ForeignKey(to='users.PersonGroup'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]
