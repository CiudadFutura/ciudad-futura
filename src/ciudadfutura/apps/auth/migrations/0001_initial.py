# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('dni', models.IntegerField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('first_name', models.CharField(max_length=255, null=True, blank=True)),
                ('last_name', models.CharField(max_length=255, null=True, blank=True)),
                ('birthdate', models.DateField(null=True, blank=True)),
                ('postal_code', models.CharField(max_length=9, null=True, blank=True)),
                ('telephone', models.CharField(max_length=32, null=True, blank=True)),
                ('cellphone', models.CharField(max_length=32, null=True, blank=True)),
                ('city', models.CharField(max_length=255, null=True, blank=True)),
                ('country', models.CharField(default=b'AR', max_length=255)),
                ('address', models.CharField(max_length=255, null=True, verbose_name='Direcci\xf3n', blank=True)),
                ('contribution', models.TextField(null=True, verbose_name='Aporte a ciudad futura', blank=True)),
                ('username', models.CharField(unique=True, max_length=255)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('legacy', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('token', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MisionMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_lead', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
