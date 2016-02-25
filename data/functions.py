# -*- coding:utf-8 -*-
from data.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import unicodedata
from django.db.models import Avg

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

def fcentro(cod_centro):
    centro = cpc.filter(id_centro = cod_centro)
    cursos = cpc.filter(id_centro = cod_centro).order_by("nome_curso").values("nome_curso","codigo_curso").distinct()

    return {'centro':centro, 'cursos':cursos}

def fcurso(cod_curso):
    curso = cpc.filter(codigo_curso = cod_curso)
    latest = curso.latest('ano')
    return {'curso':curso, 'ultimo':latest}


def fcursos():
    centros = []
    d1 = []
    d2 = []

    anotsg = tsg.latest('ano').ano
    anocpc = cpc.latest('ano').ano
    for t in tsg:
       centros.append(t.centro)
    centros = list(set(centros))

    for c in centros:
        x = []
        for t in tsg.filter(ano=anotsg):
            if c == t.centro:
                x.append(t)
        d1.append(x)

    centros = []
    for c in cpc:
        centros.append(c.id_centro)
    centros = list(set(centros))

    cpc_centro = cpc.filter(ano=anocpc).order_by("cpc_f2013")
    x = []
#    cpc_cesnorsfw = cpc_centro.filter(centro = "CESNORS FW").aggregate(Avg('cpc_f2013'))
    cpc_cefd = cpc_centro.filter(centro = "CEFD").aggregate(Avg('cpc_f2013'))
    x.append('CEFD')
    x.append('anocpc')
    x.append(cpc_cefd['cpc_f2013__avg'])
    d2.append(x)
    x = []
    cpc_ccsh = cpc_centro.filter(centro = "CCSH").aggregate(Avg('cpc_f2013'))
    x.append('CCSH')
    x.append('anocpc')
    x.append(cpc_ccsh['cpc_f2013__avg'])
    d2.append(x)
    x = []
#   cpc_ccs = cpc_centro.filter(centro = "CCS").aggregate(Avg('cpc_f2013'))
    cpc_ccr = cpc_centro.filter(centro = "CCR").aggregate(Avg('cpc_f2013'))
    x.append('CCR')
    x.append('anocpc')
    x.append(cpc_ccr['cpc_f2013__avg'])
    d2.append(x)
    x = []
    cpc_ccne = cpc_centro.filter(centro = "CCR").aggregate(Avg('cpc_f2013'))
    x.append('CCNE')
    x.append('anocpc')
    x.append(cpc_ccne['cpc_f2013__avg'])
    d2.append(x)
    x = []
    cpc_ctism = cpc_centro.filter(centro = "CTISM").aggregate(Avg('cpc_f2013'))
    x.append('CTISM')
    x.append('anocpc')
    x.append(cpc_ctism['cpc_f2013__avg'])
    d2.append(x)
    x = []
    cpc_ce = cpc_centro.filter(centro = "CE").aggregate(Avg('cpc_f2013'))
    x.append('CE')
    x.append('anocpc')
    x.append(cpc_ce['cpc_f2013__avg'])
    d2.append(x)
    x = []
#    cpc_cesnorspm = cpc_centro.filter(centro = "CESNORS PM").aggregate(Avg('cpc_f2013'))
#    cpc_udssm = cpc_centro.filter(centro = "UDSSM").aggregate(Avg('cpc_f2013'))
    cpc_cal = cpc_centro.filter(centro = "CAL").aggregate(Avg('cpc_f2013'))
    x.append('CAL')
    x.append('anocpc')
    x.append(cpc_cal['cpc_f2013__avg'])
    d2.append(x)
    x = []
    cpc_ct = cpc_centro.filter(centro = "CT").aggregate(Avg('cpc_f2013'))
    x.append('CT')
    x.append('anocpc')
    x.append(cpc_ct['cpc_f2013__avg'])
    d2.append(x)
    print d2



    cesnorsfw = cpc.filter(centro = "CESNORS FW").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro").distinct()
    cefd = cpc.filter(centro = "CEFD").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro").distinct()
    ccsh = cpc.filter(centro = "CCSH").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro").distinct()
    ccs = cpc.filter(centro = "CCS").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro").distinct()
    ccr = cpc.filter(centro = "CCR").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro").distinct()
    ccne = cpc.filter(centro = "CCNE").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro").distinct()
    ctism = cpc.filter(centro = "CTISM").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro").distinct()
    ce = cpc.filter(centro = "CE").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro").distinct()
    cesnorspm = cpc.filter(centro = "CESNORS PM").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro").distinct()
    udssm = cpc.filter(centro = "UDSSM").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro").distinct()
    cal = cpc.filter(centro = "CAL").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro").distinct()
    ct = cpc.filter(centro = "CT").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro").distinct()

    return {'d1':d1, 'd2':d2, 'cpc':cpc, 'centros':centros,
            'ccne':ccne, 'cesnorsfw':cesnorsfw, 'cefd':cefd,
            'ccsh':ccsh, 'ccs': ccs, 'ccr':ccr, 'ctism':ctism,
            'ce':ce, 'cesnorspm':cesnorspm, 'udssm':udssm, 'cal':cal,
            'ct':ct}

def favaliacao(cod_curso):

    return False
