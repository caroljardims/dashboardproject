# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0020_auto_20160224_0146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpc_geral',
            old_name='org_cad',
            new_name='org_acad',
        ),
    ]
