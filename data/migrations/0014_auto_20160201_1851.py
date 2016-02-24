# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_cpc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpc',
            name='cpc_f2013',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='t_ies_br',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='t_ies_rs',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='t_ies_sul',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='t_ifes_br',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='t_ifes_rs',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='t_ifes_sul',
            field=models.FloatField(default=0),
        ),
    ]
