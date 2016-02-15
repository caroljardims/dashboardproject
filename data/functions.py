# -*- coding:utf-8 -*-
from data.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import unicodedata

tsg = TSG.objects.all()
cpc = CPC.objects.all().order_by("ano")
igc = IGC

# funções IGC
def figc():
	igc_ufsm = IGC.objects.all().filter(nomeies = "UNIVERSIDADE FEDERAL DE SANTA MARIA").order_by("ano")
	context = {'ufsm':igc_ufsm}
	ano = IGC.objects.values('ano').distinct().order_by("ano")

	posicao = []
	total = []
	for i in ano:
	    base = 2009     #Gambiarra!!!
	    #i.values()[0]  # TESTAR
	    x = IGC.objects.filter(nomeies = "UNIVERSIDADE FEDERAL DE SANTA MARIA").order_by("ano")
	    x = x.filter(ano = i.values()[0])

	    value_igc = x.values('igc_continuo')

	    y = IGC.objects.filter(ano = i.values()[0]).order_by("ano").count()
	    total.append(y)

	    z = IGC.objects.filter(ano = i.values()[0])
	    z = z.filter(igc_continuo__gte = value_igc).count() + 1
	    posicao.append(z)

	    base = base + 1

	return {'ufsm':igc_ufsm, 'ano':ano, 'total_ies':total, 'posicao':posicao}


# funções Centros
def fcentros():
	centros = []
	d1 = []
	d2 = []

	for t in tsg:
	   centros.append(t.centro)
	centros = list(set(centros))

	for c in centros:
	    x = []
	    for t in tsg:
	        if c == t.centro:
	            x.append(t)
	    d1.append(x)

	centros = []
	for c in cpc:
	    centros.append(c.id_centro)
	centros = list(set(centros))

	for c in centros:
	    x = []
	    for t in cpc:
	        if c == t.id_centro:
	            x.append(t)
	    d2.append(x)

	return {'d1':d1, 'd2':d2}


def fcursos():
    d1 = [] #lista dos dados
    areas = []
    centros = []
    for c in cpc:
        areas.append(c.codigo_curso)
    areas = list(set(areas))

    for c in cpc:
        centros.append(c.centro)
    centros = list(set(centros))

    for a in areas:
        x = []
        for c in cpc:
            if a == c.codigo_curso:
                x.append(c)
        d1.append(x)
        
    return {'centros':centros, 'd1':d1}