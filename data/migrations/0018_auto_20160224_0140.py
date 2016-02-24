# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0017_municipios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpc',
            name='cpc_antigo',
        ),
        migrations.AddField(
            model_name='cpc',
            name='cpc_continuo',
            field=models.CharField(default=b'', max_length=4),
        ),
    ]
