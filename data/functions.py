# -*- coding:utf-8 -*-
from data.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import unicodedata
from django.db.models import Avg

tsg = TSG.objects.all()
cpc = CPC.objects.all().order_by("ano")


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

    sigla_nc = []
    sigla_nm = []
    sigla_nd = []
    sigla_nr = []
    sigla_no = []
    sigla_nf = []
    sigla_na = []
    sigla_nidd = []
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
        #query = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, nome_ies = i).values('nidd', 'nm', 'nd', 'nc', 'no', 'nf', 'nr', 'na')
        query = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, nome_ies = i).values('nc')
        if query.exists():
            nc.append(query.values('nc').first())
            sigla_nc.append(a[k])

        query = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, nome_ies = i).values('nm')
        if query.exists():
            nm.append(query.values('nm').first())
            sigla_nm.append(a[k])

        query = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, nome_ies = i).values('nd')
        if query.exists():
            nd.append(query.values('nd').first())
            sigla_nd.append(a[k])

        query = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, nome_ies = i).values('nr')
        if query.exists():
            nr.append(query.values('nr').first())
            sigla_nr.append(a[k])

        query = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, nome_ies = i).values('no')
        if query.exists():
            no.append(query.values('no').first())
            sigla_no.append(a[k])

        query = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, nome_ies = i).values('nf')
        if query.exists():
            nf.append(query.values('nf').first())
            sigla_nf.append(a[k])

        query = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, nome_ies = i).values('na')
        if query.exists():
            na.append(query.values('na').first())
            sigla_na.append(a[k])

        query = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, nome_ies = i).values('nidd')
        if query.exists():
            nidd.append(query.values('nidd').first())
            sigla_nidd.append(a[k])
            
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

    nc, sigla_nc = BSort(nc, sigla_nc)
    nm, sigla_nm = BSort(nm, sigla_nm)
    nd, sigla_nd = BSort(nd, sigla_nd)
    nr, sigla_nr = BSort(nr, sigla_nr)
    no, sigla_no = BSort(no, sigla_no)
    nf, sigla_nf = BSort(nf, sigla_nf)
    na, sigla_na = BSort(na, sigla_na)
    nidd, sigla_nidd = BSort(nidd, sigla_nidd)

    return {'ano':ano, 'nc': nc, 'nm': nm, 'nd': nd, 'nr': nr, 'no': no, 'nf':nf, 'na': na, 'nidd': nidd,
            'media_nc_br': media_nc_br, 'media_nc_rs': media_nc_rs, 'media_nm_br': media_nm_br, 'media_nm_rs': media_nm_rs,
            'media_nd_br': media_nd_br, 'media_nd_rs': media_nd_rs, 'media_nr_br': media_nr_br, 'media_nr_rs': media_nr_rs,
            'media_no_br': media_no_br, 'media_no_rs': media_no_rs, 'media_nf_br': media_nf_br, 'media_nf_rs': media_nf_rs,
            'media_na_br': media_na_br, 'media_na_rs': media_na_rs, 'media_nidd_br': media_nidd_br, 'media_nidd_rs': media_nidd_rs,
            'sigla_nc': sigla_nc, 'sigla_nm': sigla_nm, 'sigla_nd': sigla_nd, 'sigla_nr': sigla_nr, 'sigla_no': sigla_no,
            'sigla_nf': sigla_nf, 'sigla_na': sigla_na, 'sigla_nidd': sigla_nidd

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


