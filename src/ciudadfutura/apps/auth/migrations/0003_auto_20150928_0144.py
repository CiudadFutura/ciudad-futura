# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_auth', '0002_auto_20150924_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tags',
            field=models.ManyToManyField(to='ciudadfutura_auth.Tag', verbose_name='Etiquetas', blank=True),
        ),
    ]
