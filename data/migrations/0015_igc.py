# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_auto_20160201_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='IGC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ano', models.IntegerField(default=0)),
                ('codies', models.IntegerField(default=0)),
                ('nomeies', models.CharField(max_length=50)),
                ('sigla', models.CharField(max_length=15)),
                ('publica', models.IntegerField(default=0)),
                ('categoriaadm', models.CharField(max_length=30)),
                ('orgacademica', models.CharField(max_length=30)),
                ('uf', models.CharField(max_length=2)),
                ('igc_continuo', models.FloatField(default=0)),
                ('igc_faixa', models.FloatField(default=0)),
            ],
        ),
    ]
