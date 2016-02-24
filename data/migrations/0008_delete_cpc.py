# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_tsg'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CPC',
        ),
    ]
