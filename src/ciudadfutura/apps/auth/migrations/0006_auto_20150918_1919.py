# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_auth', '0005_auto_20150918_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='contribution',
            field=models.TextField(null=True, verbose_name='Aporte a ciudad futura', blank=True),
        ),
    ]
