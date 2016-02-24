# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0019_auto_20160224_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpc',
            name='CPC_FAIXA',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cpc',
            name='max_ies_br',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cpc',
            name='max_ies_rs',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cpc',
            name='max_ies_sul',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cpc',
            name='max_ifes_br',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cpc',
            name='max_ifes_rs',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cpc',
            name='max_ifes_sul',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cpc',
            name='media_ies_br',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cpc',
            name='media_ies_rs',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cpc',
            name='media_ies_sul',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cpc',
            name='media_ifes_br',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cpc',
            name='media_ifes_rs',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cpc',
            name='media_ifes_sul',
            field=models.FloatField(default=0),
        ),
    ]
