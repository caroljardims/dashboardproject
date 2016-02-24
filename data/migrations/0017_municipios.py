# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0016_auto_20160218_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='MUNICIPIOS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CODIGO_IBGE', models.IntegerField(default=0)),
                ('MUNICIPIO', models.CharField(default=b'', max_length=100)),
                ('UF', models.CharField(default=b'', max_length=2)),
                ('LATITUDE', models.FloatField(default=0)),
                ('LONGITUDE', models.FloatField(default=0)),
            ],
        ),
    ]
