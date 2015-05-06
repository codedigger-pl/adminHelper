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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(unique=True, verbose_name='username', help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=75, blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('rank', models.CharField(choices=[('pan', 'pan'), ('pani', 'pani'), ('szer.', 'szeregowy'), ('st. szer.', 'starszy szeregowy'), ('kpr.', 'kapral'), ('st. kpr.', 'starszy kapral'), ('plut.', 'plutonowy'), ('sierż', 'sierżant'), ('st. sierż.', 'starszy sierżant'), ('mł. chor.', 'młodszt chorąży'), ('chor.', 'chorąży'), ('st. chor.', 'starszy chorąży'), ('st. chor. sztab.', 'starszy chorąży sztabowy'), ('ppor.', 'podporucznik'), ('por', 'porucznik'), ('kpt.', 'kapitan'), ('ppłk', 'podpułkownik'), ('płk', 'pułkownik'), ('gen. bryg.', 'generał brygady'), ('gen. dyw.', 'generał dywizji'), ('gen. broni', 'generał broni'), ('gen.', 'generał')], max_length=20, blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', blank=True, verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', blank=True, verbose_name='user permissions', help_text='Specific permissions for this user.', to='auth.Permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('is_active', models.BooleanField(default=True)),
                ('card_number', models.CharField(max_length=15, blank=True)),
                ('rank', models.CharField(max_length=20, choices=[('pan', 'pan'), ('pani', 'pani'), ('szer.', 'szeregowy'), ('st. szer.', 'starszy szeregowy'), ('kpr.', 'kapral'), ('st. kpr.', 'starszy kapral'), ('plut.', 'plutonowy'), ('sierż', 'sierżant'), ('st. sierż.', 'starszy sierżant'), ('mł. chor.', 'młodszt chorąży'), ('chor.', 'chorąży'), ('st. chor.', 'starszy chorąży'), ('st. chor. sztab.', 'starszy chorąży sztabowy'), ('ppor.', 'podporucznik'), ('por', 'porucznik'), ('kpt.', 'kapitan'), ('ppłk', 'podpułkownik'), ('płk', 'pułkownik'), ('gen. bryg.', 'generał brygady'), ('gen. dyw.', 'generał dywizji'), ('gen. broni', 'generał broni'), ('gen.', 'generał')])),
                ('photo', models.ImageField(default='/static/img/unknown_user.jpg', null=True, upload_to='photos/', blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Osoba',
                'verbose_name_plural': 'Osoby',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=25)),
                ('description', models.TextField(blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Grupa osób',
                'verbose_name_plural': 'Grupy osób',
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
