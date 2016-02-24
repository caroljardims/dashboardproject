# -*- coding:utf-8 -*-
from data.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import unicodedata

tsg = TSG.objects.all()
cpc = CPC.objects.all().order_by("ano")

	###############
	# funções IGC #
	###############

def geralufsm():
    d1 = tsg.order_by('ano').values('centro','ano','tsgufsm').distinct()
    print d1
    return {'d1':d1}

def figc():
    igc_ufsm = IGC.objects.all().filter(nomeies = "UNIVERSIDADE FEDERAL DE SANTA MARIA").order_by("ano")

    context = {'ufsm':igc_ufsm}
    ano = IGC.objects.values('ano').distinct().order_by("ano")

    posicao = []
    total = []
    for i in ano:
        x = IGC.objects.filter(nomeies = "UNIVERSIDADE FEDERAL DE SANTA MARIA").order_by("ano")
        x = x.filter(ano = i.values()[0])

        value_igc = x.values('igc_continuo')

        y = IGC.objects.filter(ano = i.values()[0]).order_by("ano").count()
        total.append(y)

        z = IGC.objects.filter(ano = i.values()[0])
        z = z.filter(igc_continuo__gte = value_igc).count() + 1
        posicao.append(z)

    return {'ufsm':igc_ufsm, 'ano':ano, 'total_ies':total, 'posicao':posicao}

	###################
	# funções Centros #
	###################
def fcentros():
    d2 = []

    d1 = tsg.filter(centro = "CESNORS FW").order_by("ano").values("centro","ano","tsgcentro").distinct()
    #d1 = d1.latest('ano')
    print d1
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

	##################
	# funções Cursos #
	##################

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

def fcurso(cod_curso):
    curso = cpc.filter(codigo_curso = cod_curso)
    latest = curso.latest('ano')
    return {'curso':curso, 'ultimo':latest}


def fcursos():
    centros = []
    d1 = []
    d2 = []

    

    for t in tsg:
       centros.append(t.centro)
    centros = list(set(centros))

    for c in centros:
        x = []
        for t in tsg.filter(ano=2015):
            if c == t.centro:
                x.append(t)
        d1.append(x)

    centros = []
    for c in cpc:
        centros.append(c.id_centro)
    centros = list(set(centros))

    for c in centros:
        x = []
        for t in cpc.filter(ano=2014):
            if c == t.id_centro:
                x.append(t)
        d2.append(x)

    cesnorsfw = cpc.filter(centro = "CESNORS FW").order_by("nome_curso").values("nome_curso","codigo_curso").distinct()
    cefd = cpc.filter(centro = "CEFD").order_by("nome_curso").values("nome_curso","codigo_curso").distinct()
    ccsh = cpc.filter(centro = "CCSH").order_by("nome_curso").values("nome_curso","codigo_curso").distinct()
    ccs = cpc.filter(centro = "CCS").order_by("nome_curso").values("nome_curso","codigo_curso").distinct()
    ccr = cpc.filter(centro = "CCR").order_by("nome_curso").values("nome_curso","codigo_curso").distinct()
    ccne = cpc.filter(centro = "CCR").order_by("nome_curso").values("nome_curso","codigo_curso").distinct()
    ctism = cpc.filter(centro = "CTISM").order_by("nome_curso").values("nome_curso","codigo_curso").distinct()
    ce = cpc.filter(centro = "CE").order_by("nome_curso").values("nome_curso","codigo_curso").distinct()
    cesnorspm = cpc.filter(centro = "CESNORS PM").order_by("nome_curso").values("nome_curso","codigo_curso").distinct()
    udssm = cpc.filter(centro = "UDSSM").order_by("nome_curso").values("nome_curso","codigo_curso").distinct()
    cal = cpc.filter(centro = "CAL").order_by("nome_curso").values("nome_curso","codigo_curso").distinct()
    ct = cpc.filter(centro = "CT").order_by("nome_curso").values("nome_curso","codigo_curso").distinct()

    return {'d1':d1, 'd2':d2, 'cpc':cpc, 'centros':centros, 
            'ccne':ccne, 'cesnorsfw':cesnorsfw, 'cefd':cefd, 
            'ccsh':ccsh, 'ccs': ccs, 'ccr':ccr, 'ctism':ctism, 
            'ce':ce, 'cesnorspm':cesnorspm, 'udssm':udssm, 'cal':cal, 
            'ct':ct}

def favaliacao(cod_curso):

    return False
