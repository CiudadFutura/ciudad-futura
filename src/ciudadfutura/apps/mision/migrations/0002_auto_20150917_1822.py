# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_mision', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCycle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('end_pay_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='circle',
            name='created_at',
            field=models.DateTimeField(default=None, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='circle',
            name='updated_at',
            field=models.DateTimeField(default=None, auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='circle',
            name='shopping_cycle',
            field=models.ForeignKey(related_name='circles', to='ciudadfutura_mision.ShoppingCycle', null=True),
        ),
    ]
