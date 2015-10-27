# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_mision', '0002_invite'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='activation_key',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
