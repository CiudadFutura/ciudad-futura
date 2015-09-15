# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_product', '0002_auto_20150909_2231'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=255)),
                ('total', models.DecimalField(max_digits=8, decimal_places=2)),
                ('user_first_name', models.CharField(max_length=255)),
                ('user_second_name', models.CharField(max_length=255)),
                ('user_address', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=1)),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=255)),
                ('product_sku', models.CharField(max_length=255)),
                ('product_description', models.TextField()),
                ('product_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('product_real_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('product_market_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('qty', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('invoice', models.ForeignKey(related_name='items', to='ciudadfutura_order.Invoice')),
                ('product', models.ForeignKey(related_name='invoices_items', to='ciudadfutura_product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'open', max_length=32, choices=[(b'canceled', 'Canceled'), (b'STATUS2', 'Status #2'), (b'STATUS3', 'Status #1')])),
                ('reference', models.CharField(max_length=9)),
                ('total', models.DecimalField(max_digits=8, decimal_places=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=255)),
                ('product_sku', models.CharField(max_length=255)),
                ('product_description', models.TextField()),
                ('product_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('product_real_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('product_market_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('qty', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(related_name='items', to='ciudadfutura_order.Order')),
                ('product', models.ForeignKey(related_name='orders_items', to='ciudadfutura_product.Product')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='order',
            field=models.ForeignKey(related_name='invoices', to='ciudadfutura_order.Order'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='user',
            field=models.ForeignKey(related_name='invoices', to=settings.AUTH_USER_MODEL),
        ),
    ]
