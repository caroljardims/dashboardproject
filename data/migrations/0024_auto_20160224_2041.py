# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0023_auto_20160224_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpc',
            name='centro',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='cpc_antigo',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='municipio',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cpc',
            name='nome_curso',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cpc_geral',
            name='area',
            field=models.CharField(max_length=23, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='cpc_geral',
            name='cat_adm',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='cpc_geral',
            name='municipio',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cpc_geral',
            name='nome_ies',
            field=models.CharField(max_length=43),
        ),
        migrations.AlterField(
            model_name='cpc_geral',
            name='org_acad',
            field=models.CharField(max_length=22),
        ),
        migrations.AlterField(
            model_name='cpc_geral',
            name='sigla_ies',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cpc_geral',
            name='uf',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='matriculados_sisu',
            name='area',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='matriculados_sisu',
            name='campus',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='matriculados_sisu',
            name='municipio',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='matriculados_sisu',
            name='uf',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='municipios',
            name='MUNICIPIO',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='municipios',
            name='UF',
            field=models.CharField(max_length=2),
        ),
    ]
