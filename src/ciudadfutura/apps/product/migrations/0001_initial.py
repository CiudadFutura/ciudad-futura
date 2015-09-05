# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packaging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PriceChange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
                ('market_price', models.FloatField()),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sku', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('max_allowed_per_user', models.IntegerField(default=1)),
                ('price', models.FloatField()),
                ('market_price', models.FloatField()),
                ('image', models.FileField(upload_to=b'')),
                ('saleable', models.BooleanField(default=True)),
                ('packaging', models.ForeignKey(to='ciudadfutura_product.Packaging')),
                ('supplier', models.ForeignKey(to='ciudadfutura_auth.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='zones',
            field=models.ManyToManyField(to='ciudadfutura_product.Zone'),
        ),
        migrations.AddField(
            model_name='pricechange',
            name='product',
            field=models.ForeignKey(to='ciudadfutura_product.Product'),
        ),
    ]
