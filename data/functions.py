# -*- coding:utf-8 -*-
from data.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import unicodedata
from django.db.models import Avg

tsg = TSG.objects.all()
cpc = CPC.objects.all().order_by("ano")


def geralufsm():
    d1 = tsg.order_by('ano').values('centro','ano','tsgufsm').distinct()
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
    d1 = tsg.filter(ano=anotsg).order_by('tsgcentro').values('tsgcentro','ano','centro').distinct()
    centros = []
    for c in cpc:
        centros.append(c.id_centro)
    centros = list(set(centros))

    cpc_centro = cpc.filter(ano=anocpc).order_by("cpc_f2013")
    x = []
#    cpc_cesnorsfw = cpc_centro.filter(centro = "CESNORS FW").aggregate(Avg('cpc_f2013'))
    cpc_cefd = cpc_centro.filter(centro = "CEFD").aggregate(Avg('cpc_f2013'))
    x.append('CEFD')
    x.append(anocpc)
    x.append(cpc_cefd['cpc_f2013__avg'])
    d2.append(x)
    x = []
    cpc_ccsh = cpc_centro.filter(centro = "CCSH").aggregate(Avg('cpc_f2013'))
    x.append('CCSH')
    x.append(anocpc)
    x.append(cpc_ccsh['cpc_f2013__avg'])
    d2.append(x)
    x = []
#   cpc_ccs = cpc_centro.filter(centro = "CCS").aggregate(Avg('cpc_f2013'))
    cpc_ccr = cpc_centro.filter(centro = "CCR").aggregate(Avg('cpc_f2013'))
    x.append('CCR')
    x.append(anocpc)
    x.append(cpc_ccr['cpc_f2013__avg'])
    d2.append(x)
    x = []
    cpc_ccne = cpc_centro.filter(centro = "CCR").aggregate(Avg('cpc_f2013'))
    x.append('CCNE')
    x.append(anocpc)
    x.append(cpc_ccne['cpc_f2013__avg'])
    d2.append(x)
    x = []
    cpc_ctism = cpc_centro.filter(centro = "CTISM").aggregate(Avg('cpc_f2013'))
    x.append('CTISM')
    x.append(anocpc)
    x.append(cpc_ctism['cpc_f2013__avg'])
    d2.append(x)
    x = []
    cpc_ce = cpc_centro.filter(centro = "CE").aggregate(Avg('cpc_f2013'))
    x.append('CE')
    x.append(anocpc)
    x.append(cpc_ce['cpc_f2013__avg'])
    d2.append(x)
    x = []
#    cpc_cesnorspm = cpc_centro.filter(centro = "CESNORS PM").aggregate(Avg('cpc_f2013'))
#    cpc_udssm = cpc_centro.filter(centro = "UDSSM").aggregate(Avg('cpc_f2013'))
    cpc_cal = cpc_centro.filter(centro = "CAL").aggregate(Avg('cpc_f2013'))
    x.append('CAL')
    x.append(anocpc)
    x.append(cpc_cal['cpc_f2013__avg'])
    d2.append(x)
    x = []
    cpc_ct = cpc_centro.filter(centro = "CT").aggregate(Avg('cpc_f2013'))
    x.append('CT')
    x.append(anocpc)
    x.append(cpc_ct['cpc_f2013__avg'])
    d2.append(x)

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
    atual = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso).latest('ano')
    ano = atual.ano
    area = atual.area
    ufsm = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, sigla_ies = 'UFSM')

    # NC
    geral = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).order_by('-nc')
    i=0
    nc = []
    for g in geral:
        i+=1
        nc.append(g)
        if i == 20: break
    if ufsm[0] not in nc:
        nc.pop()
        nc.append(ufsm[0])
    media_nc_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nc'))
    media_nc_br = media_nc_br['nc__avg']
    media_nc_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nc'))
    media_nc_rs = media_nc_rs['nc__avg']

    # NIDD
    geral = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).order_by('-nidd')
    i=0
    nidd = []
    for g in geral:
        i+=1
        nidd.append(g)
        if i == 20: break
    if ufsm[0] not in nidd:
        nidd.pop()
        nidd.append(ufsm[0])
    media_nidd_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nidd'))
    media_nidd_br = media_nidd_br['nidd__avg']
    media_nidd_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nidd'))
    media_nidd_rs = media_nidd_rs['nidd__avg']

    # NM
    geral = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).order_by('-nm')
    i=0
    nm = []
    for g in geral:
        i+=1
        nm.append(g)
        if i == 20: break
    if ufsm[0] not in nm:
        nm.pop()
        nm.append(ufsm[0])
    media_nm_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nm'))
    media_nm_br = media_nm_br['nm__avg']
    media_nm_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nm'))
    media_nm_rs = media_nm_rs['nm__avg']

    # ND
    geral = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).order_by('-nd')
    i=0
    nd = []
    for g in geral:
        i+=1
        nd.append(g)
        if i == 20: break
    if ufsm[0] not in nd:
        nd.pop()
        nd.append(ufsm[0])
    media_nd_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nd'))
    media_nd_br = media_nd_br['nd__avg']
    media_nd_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nd'))
    media_nd_rs = media_nd_rs['nd__avg']

    # NR
    geral = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).order_by('-nr')
    i=0
    nr = []
    for g in geral:
        i+=1
        nr.append(g)
        if i == 20: break
    if ufsm[0] not in nr:
        nr.pop()
        nr.append(ufsm[0])
    media_nr_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nr'))
    media_nr_br = media_nr_br['nr__avg']
    media_nr_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nr'))
    media_nr_rs = media_nr_rs['nr__avg']

    # NO
    geral = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).order_by('-no')
    i=0
    no = []
    for g in geral:
        i+=1
        no.append(g)
        if i == 20: break
    if ufsm[0] not in no:
        no.pop()
        no.append(ufsm[0])
    media_no_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('no'))
    media_no_br = media_no_br['no__avg']
    media_no_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('no'))
    media_no_rs = media_no_rs['no__avg']

    # NF
    geral = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).order_by('-nf')
    i=0
    nf = []
    for g in geral:
        i+=1
        nf.append(g)
        if i == 20: break
    if ufsm[0] not in nf:
        nf.pop()
        nf.append(ufsm[0])
    media_nf_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nf'))
    media_nf_br = media_nf_br['nf__avg']
    media_nf_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nf'))
    media_nf_rs = media_nf_rs['nf__avg']

    # NA
    geral = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).order_by('-na')
    i=0
    na = []
    for g in geral:
        i+=1
        na.append(g)
        if i == 20: break
    if ufsm[0] not in na:
        na.pop()
        na.append(ufsm[0])
    media_na_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('na'))
    media_na_br = media_na_br['na__avg']
    media_na_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('na'))
    media_na_rs = media_na_rs['na__avg']

    return {'area':area, 'ano':ano, 'nc': nc, 'nm': nm, 'nd': nd, 'nr': nr, 'no': no, 'nf':nf, 'na': na, 'nidd': nidd,
            'media_nc_br': media_nc_br, 'media_nc_rs': media_nc_rs, 'media_nm_br': media_nm_br, 'media_nm_rs': media_nm_rs,
            'media_nd_br': media_nd_br, 'media_nd_rs': media_nd_rs, 'media_nr_br': media_nr_br, 'media_nr_rs': media_nr_rs,
            'media_no_br': media_no_br, 'media_no_rs': media_no_rs, 'media_nf_br': media_nf_br, 'media_nf_rs': media_nf_rs,
            'media_na_br': media_na_br, 'media_na_rs': media_na_rs, 'media_nidd_br': media_nidd_br, 'media_nidd_rs': media_nidd_rs,
    }

def BSort(values, ies):
    for j in range(len(values) - 1):
        for i in range(len(values) - 1):
            if values[i] < values[i+1]:
                aux = values[i]
                sigla = ies[i]
                values[i] = values[i+1]
                ies[i] = ies[i+1]
                values[i+1] = aux
                ies[i+1] = sigla

    return values, ies


