# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20151124_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpc',
            name='CATADMINISTRATIVA',
        ),
    ]
