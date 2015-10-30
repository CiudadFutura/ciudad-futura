# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_cart', '0001_initial'),
        ('ciudadfutura_auth', '0003_auto_20150928_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='misionmember',
            name='cart',
            field=models.ForeignKey(to='ciudadfutura_cart.Cart', null=True),
        ),
    ]
