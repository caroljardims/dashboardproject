# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0022_matriculados_sisu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matriculados_sisu',
            name='classificacao',
        ),
        migrations.RemoveField(
            model_name='matriculados_sisu',
            name='inscricao',
        ),
        migrations.RemoveField(
            model_name='matriculados_sisu',
            name='opcao',
        ),
    ]
