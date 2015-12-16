# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CURSO', models.CharField(max_length=20)),
                ('UF', models.CharField(max_length=2)),
                ('REGIAO', models.IntegerField(verbose_name=1)),
                ('ANO', models.IntegerField(verbose_name=4)),
                ('CPCCONTINUO', models.FloatField(default=None, null=True, blank=True)),
                ('NOTACONCLUINTES', models.FloatField(default=None, null=True, blank=True)),
                ('NOTAPADRONIZADAIDD', models.FloatField(default=None, null=True, blank=True)),
                ('NOTAPADRONIZADAMESTRES', models.FloatField(default=None, null=True, blank=True)),
                ('NOTAPADRONIZADADOUTORES', models.FloatField(default=None, null=True, blank=True)),
                ('NOMEIES', models.CharField(max_length=50)),
                ('SIGLAIES', models.CharField(max_length=15)),
                ('Publica_1_Privada_0', models.IntegerField(verbose_name=1)),
                ('CATADMINISTRATIVA', models.CharField(max_length=10)),
                ('ORGACADEMICA', models.CharField(max_length=20)),
                ('MUNICIPIOCURSO', models.CharField(max_length=50)),
                ('NOTAPADRONIZADADREGIME', models.FloatField(default=None, null=True, blank=True)),
                ('NOTAPADRONIZADAPEDAG', models.FloatField(default=None, null=True, blank=True)),
                ('CPC_FAIXA', models.FloatField(default=None, null=True, blank=True)),
                ('NOTAPADRONIZADAINFRA', models.FloatField(default=None, null=True, blank=True)),
                ('INGRESSANTESPARTICIPANTES', models.IntegerField(verbose_name=5)),
                ('INGRESSANTESINSCRITOS', models.IntegerField(verbose_name=5)),
                ('COD_CURSO', models.IntegerField(verbose_name=5)),
                ('COD_IES', models.IntegerField(verbose_name=5)),
                ('AMPLIACAOFORMACAO_NA', models.FloatField(default=None, null=True, blank=True)),
                ('CPC_FORMULA2013', models.FloatField(default=None, null=True, blank=True)),
            ],
        ),
    ]
