# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'new', max_length=32, choices=[(b'new', 'New order'), (b'canceled', 'Canceled'), (b'on_hold', 'On hold'), (b'pending_payment', 'Pending payment'), (b'pending_received', 'Pending received'), (b'shipped', 'Order shipped'), (b'paid', 'Paid'), (b'closed', 'Closed')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
        ),
    ]
