# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_delete_cpc'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_id', models.IntegerField(default=0)),
                ('ano', models.IntegerField(default=0)),
                ('municipio', models.CharField(default=b'', max_length=50)),
                ('codigo_curso', models.IntegerField(default=0)),
                ('nome_curso', models.CharField(default=b'', max_length=50)),
                ('centro', models.CharField(default=b'', max_length=10, blank=True)),
                ('cpc_antigo', models.CharField(default=b'', max_length=4, blank=True)),
                ('nc', models.FloatField(default=0)),
                ('nidd', models.FloatField(default=0)),
                ('nm', models.FloatField(default=0)),
                ('nd', models.FloatField(default=0)),
                ('nr', models.IntegerField(default=0)),
                ('no', models.FloatField(default=0)),
                ('nf', models.FloatField(default=0)),
                ('na', models.FloatField(default=0)),
                ('cpc_f2013', models.CharField(default=b'', max_length=4, blank=True)),
                ('t_ies_br', models.CharField(default=b'', max_length=10, blank=True)),
                ('t_ies_sul', models.CharField(default=b'', max_length=10, blank=True)),
                ('t_ies_rs', models.CharField(default=b'', max_length=10, blank=True)),
                ('t_ifes_br', models.CharField(default=b'', max_length=10, blank=True)),
                ('t_ifes_sul', models.CharField(default=b'', max_length=10, blank=True)),
                ('t_ifes_rs', models.CharField(default=b'', max_length=10, blank=True)),
                ('id_centro', models.IntegerField(default=0)),
                ('posicaobrasilcpc', models.IntegerField(default=0)),
                ('posicaorscpc', models.IntegerField(default=0)),
                ('posicaopublicabrasilcpc', models.IntegerField(default=0)),
                ('posicaopublicarscpc', models.IntegerField(default=0)),
                ('posicaosulcpc', models.IntegerField(default=0)),
                ('posicaoifescpc', models.IntegerField(default=0)),
                ('posicaobrasilinfra', models.IntegerField(default=0)),
                ('posicaorsinfra', models.IntegerField(default=0)),
                ('posicaopublicabrasilinfra', models.IntegerField(default=0)),
                ('posicaopublicarsinfra', models.IntegerField(default=0)),
                ('posicaosulinfra', models.IntegerField(default=0)),
                ('posicaoifesinfra', models.IntegerField(default=0)),
                ('posicaobrasilpedag', models.IntegerField(default=0)),
                ('posicaorspedag', models.IntegerField(default=0)),
                ('posicaopublicabrasilpedag', models.IntegerField(default=0)),
                ('posicaopublicarspedag', models.IntegerField(default=0)),
                ('posicaosulpedag', models.IntegerField(default=0)),
                ('posicaoifespedag', models.IntegerField(default=0)),
                ('posicaobrasilregime', models.IntegerField(default=0)),
                ('posicaorsregime', models.IntegerField(default=0)),
                ('posicaopublicabrasilregime', models.IntegerField(default=0)),
                ('posicaopublicarsregime', models.IntegerField(default=0)),
                ('posicaosulregime', models.IntegerField(default=0)),
                ('posicaoifesregime', models.IntegerField(default=0)),
                ('posicaobrasildoutor', models.IntegerField(default=0)),
                ('posicaorsdoutor', models.IntegerField(default=0)),
                ('posicaopublicabrasildoutor', models.IntegerField(default=0)),
                ('posicaopublicarsdoutor', models.IntegerField(default=0)),
                ('posicaosuldoutor', models.IntegerField(default=0)),
                ('posicaoifesdoutor', models.IntegerField(default=0)),
                ('posicaobrasilidd', models.IntegerField(default=0)),
                ('posicaorsidd', models.IntegerField(default=0)),
                ('posicaopublicabrasilidd', models.IntegerField(default=0)),
                ('posicaopublicarsidd', models.IntegerField(default=0)),
                ('posicaosulidd', models.IntegerField(default=0)),
                ('posicaoifesidd', models.IntegerField(default=0)),
                ('posicaobrasilenade', models.IntegerField(default=0)),
                ('posicaorsenade', models.IntegerField(default=0)),
                ('posicaopublicabrasilenade', models.IntegerField(default=0)),
                ('posicaopublicarsenade', models.IntegerField(default=0)),
                ('posicaosulenade', models.IntegerField(default=0)),
                ('posicaoifesenade', models.IntegerField(default=0)),
                ('posicaobrasilmestre', models.IntegerField(default=0)),
                ('posicaorsmestre', models.IntegerField(default=0)),
                ('posicaopublicabrasilmestre', models.IntegerField(default=0)),
                ('posicaopublicarsmestre', models.IntegerField(default=0)),
                ('posicaosulmestre', models.IntegerField(default=0)),
                ('posicaoifesmestre', models.IntegerField(default=0)),
                ('posicaobrasilampliacao', models.IntegerField(default=0)),
                ('posicaorsampliacao', models.IntegerField(default=0)),
                ('posicaopublicabrasilampliacao', models.IntegerField(default=0)),
                ('posicaopublicarsampliacao', models.IntegerField(default=0)),
                ('posicaosulampliacao', models.IntegerField(default=0)),
                ('posicaoifesampliacao', models.IntegerField(default=0)),
                ('distanciabrasilcpc', models.FloatField(default=0)),
                ('distanciarscpc', models.FloatField(default=0)),
                ('distanciapublicacpc', models.FloatField(default=0)),
                ('distanciapublicarscpc', models.IntegerField(default=0)),
                ('distanciasulcpc', models.FloatField(default=0)),
                ('distanciaifescpc', models.FloatField(default=0)),
                ('distanciabrasilenade', models.FloatField(default=0)),
                ('distanciarsenade', models.FloatField(default=0)),
                ('distanciapublicaenade', models.FloatField(default=0)),
                ('distanciapublicarsenade', models.FloatField(default=0)),
                ('distanciasulenade', models.FloatField(default=0)),
                ('distanciaifesenade', models.FloatField(default=0)),
            ],
        ),
    ]