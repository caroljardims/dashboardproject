# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0021_auto_20160224_0203'),
    ]

    operations = [
        migrations.CreateModel(
            name='MATRICULADOS_SISU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campus', models.CharField(default=b'', max_length=50)),
                ('area', models.CharField(default=b'', max_length=50)),
                ('uf', models.CharField(default=b'', max_length=2)),
                ('municipio', models.CharField(default=b'', max_length=50)),
                ('inscricao', models.IntegerField(default=0)),
                ('opcao', models.IntegerField(default=0)),
                ('classificacao', models.IntegerField(default=0)),
            ],
        ),
    ]
