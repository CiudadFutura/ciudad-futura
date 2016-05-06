# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_auth', '0009_auto_20160103_0011'),
        ('ciudadfutura_order', '0003_auto_20160119_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='supplier',
            field=models.ForeignKey(related_name='suppliers', to='ciudadfutura_auth.Supplier', null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(related_name='items', to='ciudadfutura_order.Order'),
        ),
    ]
