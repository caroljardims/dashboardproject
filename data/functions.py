# -*- coding:utf-8 -*-
from data.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import unicodedata
from django.db.models import Avg

tsg = TSG.objects.all()
cpc = CPC.objects.all().order_by('ano')

	###############
	# funções IGC #
	###############

def geralufsm():
    d1 = tsg.order_by('ano').values('centro','ano','tsgufsm').distinct()
    print d1
    return {'d1':d1}

def figc():
    igc_ufsm = IGC.objects.all().filter(nomeies = 'UNIVERSIDADE FEDERAL DE SANTA MARIA').order_by('ano')

    context = {'ufsm':igc_ufsm}
    ano = IGC.objects.values('ano').distinct().order_by('ano')

    posicao = []
    total = []
    for i in ano:
        x = IGC.objects.filter(nomeies = 'UNIVERSIDADE FEDERAL DE SANTA MARIA').order_by('ano')
        x = x.filter(ano = i.values()[0])

        value_igc = x.values('igc_continuo')

        y = IGC.objects.filter(ano = i.values()[0]).order_by('ano').count()
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

    d1 = tsg.filter(centro = 'CESNORS FW').order_by('ano').values('centro','ano','tsgcentro').distinct()
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
    cursos = cpc.filter(id_centro = cod_centro).order_by('nome_curso').values('nome_curso','codigo_curso').distinct()
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

    for c in centros:
        x = []
        for t in cpc.filter(ano=anocpc):
            if c == t.id_centro:
                x.append(t)
        d2.append(x)

    cesnorsfw = cpc.filter(centro = 'CESNORS FW').order_by('nome_curso').values('nome_curso','codigo_curso','id_centro').distinct()
    cefd = cpc.filter(centro = 'CEFD').order_by('nome_curso').values('nome_curso','codigo_curso','id_centro').distinct()
    ccsh = cpc.filter(centro = 'CCSH').order_by('nome_curso').values('nome_curso','codigo_curso','id_centro').distinct()
    ccs = cpc.filter(centro = 'CCS').order_by('nome_curso').values('nome_curso','codigo_curso','id_centro').distinct()
    ccr = cpc.filter(centro = 'CCR').order_by('nome_curso').values('nome_curso','codigo_curso','id_centro').distinct()
    ccne = cpc.filter(centro = 'CCR').order_by('nome_curso').values('nome_curso','codigo_curso','id_centro').distinct()
    ctism = cpc.filter(centro = 'CTISM').order_by('nome_curso').values('nome_curso','codigo_curso','id_centro').distinct()
    ce = cpc.filter(centro = 'CE').order_by('nome_curso').values('nome_curso','codigo_curso','id_centro').distinct()
    cesnorspm = cpc.filter(centro = 'CESNORS PM').order_by('nome_curso').values('nome_curso','codigo_curso','id_centro').distinct()
    udssm = cpc.filter(centro = 'UDSSM').order_by('nome_curso').values('nome_curso','codigo_curso','id_centro').distinct()
    cal = cpc.filter(centro = 'CAL').order_by('nome_curso').values('nome_curso','codigo_curso','id_centro').distinct()
    ct = cpc.filter(centro = 'CT').order_by('nome_curso').values('nome_curso','codigo_curso','id_centro').distinct()

    return {'d1':d1, 'd2':d2, 'cpc':cpc, 'centros':centros,
            'ccne':ccne, 'cesnorsfw':cesnorsfw, 'cefd':cefd,
            'ccsh':ccsh, 'ccs': ccs, 'ccr':ccr, 'ctism':ctism,
            'ce':ce, 'cesnorspm':cesnorspm, 'udssm':udssm, 'cal':cal,
            'ct':ct}

def favaliacao(cod_curso):
    a = [
        'UNICAMP',
        'UFRGS',
        'UNILA',
        'UFSM',
        'UNIFESP',
        'UFSC',
        'UFRJ',
        'UFV',
        'UFABC',
        'UFLA',
        'UNB',
        'UFSCAR',
        'UNESP',
        'UFCSPA',
        'UENF',
        'UFMG',
        'UFJF',
        'UFPE',
        'PUC-RJ',
        'UFPR'
    ]

    ies = [
        'UNIVERSIDADE ESTADUAL DE CAMPINAS',
        'UNIVERSIDADE FEDERAL DO RIO GRANDE DO SUL',
        'UNIVERSIDADE FEDERAL DA INTEGRAÇÃO LATINO-AMERICANA',
        'UNIVERSIDADE FEDERAL DE SANTA MARIA',
        'UNIVERSIDADE FEDERAL DE SÃO PAULO',
        'UNIVERSIDADE FEDERAL DE SANTA CATARINA',
        'UNIVERSIDADE FEDERAL DO RIO DE JANEIRO',
        'UNIVERSIDADE FEDERAL DE VIÇOSA',
        'UNIVERSIDADE FEDERAL DO ABC',
        'UNIVERSIDADE FEDERAL DE LAVRAS',
        'UNIVERSIDADE DE BRASÍLIA',
        'UNIVERSIDADE FEDERAL DE SÃO CARLOS',
        'UNIVERSIDADE ESTADUAL PAULISTA',
        'UNIVERSIDADE FEDERAL DE CIÊNCIAS DA SAÚDE DE PORTO ALEGRE',
        'UNIVERSIDADE ESTADUAL DO NORTE FLUMINENSE DARCY RIBEIRO',
        'UNIVERSIDADE FEDERAL DE MINAS GERAIS',
        'UNIVERSIDADE FEDERAL DE JUIZ DE FORA',
        'UNIVERSIDADE FEDERAL DE PELOTAS',
        'PONTIFÍCIA UNIVERSIDADE CATÓLICA DO RIO DE JANEIRO',
        'UNIVERSIDADE FEDERAL DO PARANÁ'
    ]

    sigla = []
    nidd = []
    nc = []
    nm = []
    nd = []
    nr = []
    no = []
    nf = []
    na =[]

    tmp = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso).values('ano').order_by('ano').distinct()
    ano = tmp.latest('ano').values()[0]
    k = 0
    for i in ies:
        query = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, nome_ies = i).values('nidd', 'nm', 'nd', 'nc', 'no', 'nf', 'nr', 'na')
        nc.append(query.values('nc').first())
        nm.append(query.values('nm').first())
        nd.append(query.values('nd').first())
        nr.append(query.values('nr').first())
        no.append(query.values('no').first())
        nf.append(query.values('nf').first())
        na.append(query.values('na').first())
        nidd.append(query.values('nidd').first())
        sigla.append(a[k])
        k = k + 1

    media_nc_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nc'))
    media_nc_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nc'))
    
    media_nm_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nm'))
    media_nm_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nm'))

    media_nd_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nd'))
    media_nd_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nd'))

    media_nr_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nr'))
    media_nr_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nr'))

    media_no_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('no'))
    media_no_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('no'))

    media_nf_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nf'))
    media_nf_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nf'))

    media_na_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('na'))
    media_na_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('na'))

    media_nidd_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nidd'))
    media_nidd_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nidd'))

    return {'ano':ano, 'sigla': sigla, 'nc': nc, 'nm': nm, 'nd': nd, 'nr': nr, 'no': no, 'nf':nf, 'na': na, 'nidd': nidd,
            'media_nc_br': media_nc_br, 'media_nc_rs': media_nc_rs, 'media_nm_br': media_nm_br, 'media_nm_rs': media_nm_rs,
            'media_nd_br': media_nd_br, 'media_nd_rs': media_nd_rs, 'media_nr_br': media_nr_br, 'media_nr_rs': media_nr_rs,
            'media_no_br': media_no_br, 'media_no_rs': media_no_rs, 'media_nf_br': media_nf_br, 'media_nf_rs': media_nf_rs,
            'media_na_br': media_na_br, 'media_na_rs': media_na_rs, 'media_nidd_br': media_nidd_br, 'media_nidd_rs': media_nidd_rs
    }
