# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20151124_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpc',
            old_name='CURSO',
            new_name='AREA',
        ),
        migrations.RenameField(
            model_name='cpc',
            old_name='COD_CURSO',
            new_name='COD_AREA',
        ),
        migrations.RenameField(
            model_name='cpc',
            old_name='Publica_1_Privada_0',
            new_name='PUB_PRIV',
        ),
    ]
