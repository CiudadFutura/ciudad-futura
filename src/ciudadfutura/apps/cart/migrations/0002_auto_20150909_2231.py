# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='market_price',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
    ]
