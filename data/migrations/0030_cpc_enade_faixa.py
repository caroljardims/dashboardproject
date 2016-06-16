# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0029_auto_20160616_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpc',
            name='enade_faixa',
            field=models.IntegerField(default=0),
        ),
    ]
