# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadfutura_auth', '0002_auto_20150905_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='person',
            field=models.OneToOneField(null=True, default=None, to='ciudadfutura_auth.Person'),
        ),
    ]
