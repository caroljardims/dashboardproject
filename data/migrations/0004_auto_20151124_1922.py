# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20151124_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpc',
            name='AMPLIACAOFORMACAO_NA',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='CPCCONTINUO',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='CPC_FAIXA',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='CPC_FORMULA2013',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='NOTACONCLUINTES',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='NOTAPADRONIZADADOUTORES',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='NOTAPADRONIZADADREGIME',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='NOTAPADRONIZADAIDD',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='NOTAPADRONIZADAINFRA',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='NOTAPADRONIZADAMESTRES',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='NOTAPADRONIZADAPEDAG',
            field=models.FloatField(default=None),
        ),
    ]
