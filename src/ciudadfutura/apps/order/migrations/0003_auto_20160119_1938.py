# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_mision', '0004_invite_code'),
        ('ciudadfutura_order', '0002_auto_20160106_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AddField(
            model_name='invoice',
            name='status',
            field=models.CharField(default=b'new', max_length=32, choices=[(b'new', 'New order'), (b'canceled', 'Canceled'), (b'on_hold', 'On hold'), (b'pending_payment', 'Pending payment'), (b'pending_received', 'Pending received'), (b'shipped', 'Order shipped'), (b'paid', 'Paid'), (b'closed', 'Closed')]),
        ),
        migrations.AddField(
            model_name='order',
            name='shopping_cycle',
            field=models.ForeignKey(related_name='cycles', to='ciudadfutura_mision.ShoppingCycle', null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(default=b'added', max_length=32, choices=[(b'added', 'Added'), (b'deleted', 'Deleted')]),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(related_name='suppliers', to='ciudadfutura_order.Order'),
        ),
    ]
