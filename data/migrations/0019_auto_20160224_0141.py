# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0018_auto_20160224_0140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpc',
            old_name='cpc_continuo',
            new_name='cpc_antigo',
        ),
    ]
