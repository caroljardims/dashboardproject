# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-16 12:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0026_matriculados_sisu_codigo_curso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpc',
            old_name='cpc_antigo',
            new_name='cpc_continuo',
        ),
    ]
