# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_mision', '0003_invite_activation_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='code',
            field=models.CharField(default=None, unique=True, max_length=255),
            preserve_default=False,
        ),
    ]
