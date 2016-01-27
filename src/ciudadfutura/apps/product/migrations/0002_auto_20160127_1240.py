# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sub_category', models.OneToOneField(related_name='category', null=True, blank=True, to='ciudadfutura_product.Category')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='zones',
            field=models.ManyToManyField(to='ciudadfutura_product.Zone', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='ciudadfutura_product.Category', blank=True),
        ),
    ]
