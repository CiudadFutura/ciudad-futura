# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_auth', '0004_misionmember_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebook',
            name='user',
            field=models.OneToOneField(related_name='facebook', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='misionmember',
            name='user',
            field=models.OneToOneField(related_name='member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='user',
            field=models.OneToOneField(related_name='supplier', to=settings.AUTH_USER_MODEL),
        ),
    ]
