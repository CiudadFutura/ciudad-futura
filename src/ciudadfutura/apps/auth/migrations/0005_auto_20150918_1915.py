# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_auth', '0004_auto_20150917_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='contribution',
            field=models.TextField(null=True, verbose_name='Aporte a ciudad futura'),
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Direcci\xf3n'),
        ),
        migrations.AlterField(
            model_name='person',
            name='country',
            field=models.CharField(default=b'AR', max_length=255),
        ),
        migrations.AddField(
            model_name='person',
            name='relationships',
            field=models.ManyToManyField(to='ciudadfutura_auth.Relationship', verbose_name='Vinculos'),
        ),
    ]
