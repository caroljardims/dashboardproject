# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0024_auto_20160224_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpc_geral',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cpc_geral',
            name='area',
            field=models.CharField(max_length=23),
        ),
    ]
