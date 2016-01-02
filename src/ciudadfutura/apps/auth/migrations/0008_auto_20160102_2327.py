# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_auth', '0007_auto_20160102_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to=b'user/avatars', null=True, verbose_name='Foto de perfil', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(null=True, verbose_name='Fecha Nacimiento', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=255, null=True, verbose_name='Ciudad', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255, null=True, verbose_name='First name', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Last name', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='postal_code',
            field=models.CharField(max_length=9, null=True, verbose_name='C\xf3digo Postal', blank=True),
        ),
    ]
