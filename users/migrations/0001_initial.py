# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SysUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], max_length=30, unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name='username')),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('email', models.EmailField(max_length=75, blank=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rank', models.CharField(max_length=20, blank=True, choices=[('pan', 'pan'), ('pani', 'pani'), ('szer.', 'szeregowy'), ('st. szer.', 'starszy szeregowy'), ('kpr.', 'kapral'), ('st. kpr.', 'starszy kapral'), ('plut.', 'plutonowy'), ('sierż', 'sierżant'), ('st. sierż.', 'starszy sierżant'), ('mł. chor.', 'młodszt chorąży'), ('chor.', 'chorąży'), ('st. chor.', 'starszy chorąży'), ('st. chor. sztab.', 'starszy chorąży sztabowy'), ('ppor.', 'podporucznik'), ('por', 'porucznik'), ('kpt.', 'kapitan'), ('ppłk', 'podpułkownik'), ('płk', 'pułkownik'), ('gen. bryg.', 'generał brygady'), ('gen. dyw.', 'generał dywizji'), ('gen. broni', 'generał broni'), ('gen.', 'generał')])),
                ('groups', models.ManyToManyField(related_query_name='user', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions', related_name='user_set')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('is_active', models.BooleanField(default=True)),
                ('card_number', models.CharField(max_length=15, blank=True)),
                ('rank', models.CharField(max_length=20, choices=[('pan', 'pan'), ('pani', 'pani'), ('szer.', 'szeregowy'), ('st. szer.', 'starszy szeregowy'), ('kpr.', 'kapral'), ('st. kpr.', 'starszy kapral'), ('plut.', 'plutonowy'), ('sierż', 'sierżant'), ('st. sierż.', 'starszy sierżant'), ('mł. chor.', 'młodszt chorąży'), ('chor.', 'chorąży'), ('st. chor.', 'starszy chorąży'), ('st. chor. sztab.', 'starszy chorąży sztabowy'), ('ppor.', 'podporucznik'), ('por', 'porucznik'), ('kpt.', 'kapitan'), ('ppłk', 'podpułkownik'), ('płk', 'pułkownik'), ('gen. bryg.', 'generał brygady'), ('gen. dyw.', 'generał dywizji'), ('gen. broni', 'generał broni'), ('gen.', 'generał')])),
                ('photo', models.ImageField(default='/static/img/unknown_user.jpg', blank=True, null=True, upload_to='photos/')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=25, unique=True)),
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
