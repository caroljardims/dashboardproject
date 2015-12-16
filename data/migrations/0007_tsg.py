# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_remove_cpc_catadministrativa'),
    ]

    operations = [
        migrations.CreateModel(
            name='TSG',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CENTRO', models.CharField(max_length=50)),
                ('ANO', models.IntegerField(default=0)),
                ('CODCURSO', models.IntegerField(default=0)),
                ('NOMECURSO', models.CharField(max_length=50)),
                ('INGRESSANTES', models.IntegerField(default=0)),
                ('FORMADOS', models.IntegerField(default=0)),
                ('MATRICULADOS', models.IntegerField(default=0)),
                ('TSGTAXA', models.FloatField(default=0)),
                ('TSGCENTRO', models.FloatField(default=0)),
                ('TSGUFSM', models.FloatField(default=0)),
                ('ANOINGRESSO', models.IntegerField(default=0)),
            ],
        ),
    ]
