# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0025_auto_20160224_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='matriculados_sisu',
            name='codigo_curso',
            field=models.IntegerField(default=0),
        ),
    ]
