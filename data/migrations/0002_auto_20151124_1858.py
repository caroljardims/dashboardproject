# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpc',
            name='ANO',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='COD_CURSO',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='COD_IES',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='INGRESSANTESINSCRITOS',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='INGRESSANTESPARTICIPANTES',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='Publica_1_Privada_0',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='REGIAO',
            field=models.IntegerField(default=0),
        ),
    ]
