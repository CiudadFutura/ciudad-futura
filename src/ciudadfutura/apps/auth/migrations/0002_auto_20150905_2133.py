# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_auth', '0001_initial'),
        ('ciudadfutura_mision', '0001_initial'),
        ('ciudadfutura_product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='default_zones',
            field=models.ManyToManyField(to='ciudadfutura_product.Zone'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='user',
            field=models.ForeignKey(related_name='supplier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='misionmember',
            name='circle',
            field=models.ForeignKey(blank=True, to='ciudadfutura_mision.Circle', null=True),
        ),
        migrations.AddField(
            model_name='misionmember',
            name='user',
            field=models.ForeignKey(related_name='member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='facebook',
            name='user',
            field=models.ForeignKey(related_name='facebook', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='person',
            field=models.OneToOneField(to='ciudadfutura_auth.Person'),
        ),
    ]
