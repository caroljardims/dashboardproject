# -*- coding:utf-8 -*-
from data.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import unicodedata
from django.db.models import Avg

tsg = TSG.objects.all()
cpc = CPC.objects.all().order_by("ano")

centrosmenu = cpc.order_by("centro").values("centro","id_centro").distinct()
cursosmenu = []
benchs = ["UFSM","UFRGS","FAAPF","UCS","UERGS","FEEVALE","UFPEL","UNICRUZ","PUCRS","UNIJUI","UPF","UFCSPA","URI","UCPEL","UNISC","UNISINOS","UNIPAMPA","ULBRA","UNIFRA","FADISMA","FISMA","FURG","FAPAS","URCAMP","UNIJUÍ"]

cal = cpc.filter(centro = "CAL").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro", "centro").distinct()
cursosmenu.append(cal)
ccne = cpc.filter(centro = "CCNE").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro", "centro").distinct()
cursosmenu.append(ccne)
ccr = cpc.filter(centro = "CCR").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro", "centro").distinct()
cursosmenu.append(ccr)
ccs = cpc.filter(centro = "CCS").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro", "centro").distinct()
cursosmenu.append(ccs)
ccsh = cpc.filter(centro = "CCSH").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro", "centro").distinct()
cursosmenu.append(ccsh)
ce = cpc.filter(centro = "CE").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro", "centro").distinct()
cursosmenu.append(ce)
cesnorsfw = cpc.filter(centro = "CESNORS FW").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro").distinct()
cefd = cpc.filter(centro = "CEFD").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro", "centro").distinct()
cursosmenu.append(cefd)
ct = cpc.filter(centro = "CT").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro", "centro").distinct()
cursosmenu.append(ct)
ctism = cpc.filter(centro = "CTISM").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro", "centro").distinct()
cursosmenu.append(ctism)
cesnorspm = cpc.filter(centro = "CESNORS PM").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro", "centro").distinct()
udssm = cpc.filter(centro = "UDSSM").order_by("nome_curso").values("nome_curso","codigo_curso","id_centro", "centro").distinct()

def geralufsm():
    d1 = tsg.order_by('ano').values('centro','ano','tsgufsm').distinct()
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

    return {'d1':d1,'ufsm':igc_ufsm,'ano':ano,'total_ies':total,'posicao':posicao,'cursosmenu':cursosmenu, 'centrosmenu':centrosmenu}

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
    anos = centro.values('ano').distinct()
    a = []
    c = []
    for ano in anos:
        a.append(ano)
    x1 = a[-1]
    x2 = a[-2]
    x3 = x1['ano'] - x2['ano']
    if x3 > 2:
        ano = a.pop()
        ano = int(ano['ano'])
        cursos = centro.filter(ano = ano).order_by('cpc_f2013').values('codigo_curso', 'nome_curso', 'cpc_f2013','ano').distinct()
        for curso in cursos:
                if curso['cpc_f2013'] > 0:
                    c.append(curso)
    else:
        for i in range(3): # 3 últimos anos, último triênio
            ano = a.pop()
            ano = int(ano['ano'])
            cursos = centro.filter(ano = ano).order_by('cpc_f2013').values('codigo_curso', 'nome_curso', 'cpc_f2013','ano').distinct()
            for curso in cursos:
                if curso['cpc_f2013'] > 0:
                    c.append(curso)
    cursos = sorted(c, key=lambda k: k['cpc_f2013'], reverse = False)

    d1 = []
    aux = []
    for i in anos: aux.append(i['ano'])
    yearlist = aux[::-1]
    for y in yearlist:
        x = []
        z = []
        aux = y
        for c in range(3):
            if centro.filter(ano = aux) is not None:
                aux2 = centro.filter(ano = aux).values('cpc_f2013')
                aux2 = map(lambda d: d['cpc_f2013'], aux2)
                if len(aux2) > 0:
                    for m in aux2:
                        x.append(m)
            aux = aux + 1
        media = reduce(lambda a, b: a + b, x)/len(x)
            # centro, ano, media cpc
        d1.append([centro[0].centro, y,y+2, media])
        # print d1
    centro = d1[::-1]

    return {'centro':centro, 'cursos':cursos, 'ano':ano, 'cursosmenu':cursosmenu, 'centrosmenu':centrosmenu}

def fcurso(cod_curso):
    curso = cpc.filter(codigo_curso = cod_curso)
    atsg = tsg.filter(codcurso = cod_curso)
    # for a in atsg: print a.nomecurso
    latest = curso.latest('ano')
    atual = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso).latest('ano')
    ano = atual.ano
    area = atual.area
    ufsm = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, sigla_ies = 'UFSM')
    cursos = []

    for b in benchs:
        var = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, sigla_ies = b)
        for v in var:
            cursos.append(v)
    # NC
    nc = []
    for b in benchs:
        var = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, sigla_ies = b)
        for v in var:
            nc.append(v)
    nc = sorted(nc, key=lambda x: x.nc, reverse = True)
    nc = nc[:20]
    media_nc_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nc'))
    media_nc_br = media_nc_br['nc__avg']
    media_nc_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nc'))
    media_nc_rs = media_nc_rs['nc__avg']

    # NIDD
    nidd = []
    for b in benchs:
        var = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, sigla_ies = b).order_by('nidd')
        for v in var:
            nidd.append(v)
    nidd = sorted(nidd, key=lambda x: x.nidd, reverse = True)
    nidd = nidd[:20]
    media_nidd_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nidd'))
    media_nidd_br = media_nidd_br['nidd__avg']
    media_nidd_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nidd'))
    media_nidd_rs = media_nidd_rs['nidd__avg']

    # NM
    nm = []
    for b in benchs:
        var = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, sigla_ies = b).order_by('nm')
        for v in var:
            nm.append(v)
    nm = sorted(nm, key=lambda x: x.nm, reverse = True)
    nm = nm[:20]
    media_nm_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nm'))
    media_nm_br = media_nm_br['nm__avg']
    media_nm_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nm'))
    media_nm_rs = media_nm_rs['nm__avg']

    # ND
    nd = []
    for b in benchs:
        var = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, sigla_ies = b).order_by('nd')
        for v in var:
            nd.append(v)
    nd = sorted(nd, key=lambda x: x.nd, reverse = True)
    nd = nd[:20]
    media_nd_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nd'))
    media_nd_br = media_nd_br['nd__avg']
    media_nd_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nd'))
    media_nd_rs = media_nd_rs['nd__avg']

    # NR
    nr = []
    for b in benchs:
        var = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, sigla_ies = b).order_by('nr')
        for v in var:
            nr.append(v)
    nr = sorted(nr, key=lambda x: x.nr, reverse = True)
    nr = nr[:20]
    media_nr_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nr'))
    media_nr_br = media_nr_br['nr__avg']
    media_nr_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nr'))
    media_nr_rs = media_nr_rs['nr__avg']

    # NO
    no = []
    for b in benchs:
        var = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, sigla_ies = b).order_by('no')
        for v in var:
            no.append(v)
    no = sorted(no, key=lambda x: x.no, reverse = True)
    no = no[:20]
    media_no_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('no'))
    media_no_br = media_no_br['no__avg']
    media_no_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('no'))
    media_no_rs = media_no_rs['no__avg']

    # NF
    nf = []
    for b in benchs:
        var = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, sigla_ies = b).order_by('nf')
        for v in var:
            nf.append(v)
    nf = sorted(nf, key=lambda x: x.nf, reverse = True)
    nf = nf[:20]
    media_nf_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('nf'))
    media_nf_br = media_nf_br['nf__avg']
    media_nf_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('nf'))
    media_nf_rs = media_nf_rs['nf__avg']

    # NA
    na = []
    for b in benchs:
        var = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, sigla_ies = b).order_by('na')
        for v in var:
            na.append(v)
    na = sorted(na, key=lambda x: x.na, reverse = True)
    na = na[:20]
    media_na_br = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano).aggregate(Avg('na'))
    media_na_br = media_na_br['na__avg']
    media_na_rs = CPC_GERAL.objects.all().filter(codigo_curso = cod_curso, ano = ano, uf='RS').aggregate(Avg('na'))
    media_na_rs = media_na_rs['na__avg']

    return {'area':area, 'ano':ano, 'nc': nc, 'nm': nm, 'nd': nd, 'nr': nr, 'no': no, 'nf':nf, 'na': na, 'nidd': nidd,
            'media_nc_br': media_nc_br, 'media_nc_rs': media_nc_rs, 'media_nm_br': media_nm_br, 'media_nm_rs': media_nm_rs,
            'media_nd_br': media_nd_br, 'media_nd_rs': media_nd_rs, 'media_nr_br': media_nr_br, 'media_nr_rs': media_nr_rs,
            'media_no_br': media_no_br, 'media_no_rs': media_no_rs, 'media_nf_br': media_nf_br, 'media_nf_rs': media_nf_rs,
            'media_na_br': media_na_br, 'media_na_rs': media_na_rs, 'media_nidd_br': media_nidd_br, 'media_nidd_rs': media_nidd_rs,
            'curso':curso, 'ultimo':latest, 'cursosmenu':cursosmenu, 'centrosmenu':centrosmenu
    }

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

    for a in range(3):
        cpc_centro = cpc.filter(ano=anocpc).order_by("cpc_f2013")
        x = []
    #    cpc_cesnorsfw = cpc_centro.filter(centro = "CESNORS FW").aggregate(Avg('cpc_f2013'))

        cpc_cefd = cpc_centro.filter(centro = "CEFD").aggregate(Avg('cpc_f2013'))
        x.append('CEFD')
        x.append(anocpc)
        x.append(cpc_cefd['cpc_f2013__avg'])
        if cpc_cefd['cpc_f2013__avg'] is not None : d2.append(x)
        x = []

        cpc_ccsh = cpc_centro.filter(centro = "CCSH").aggregate(Avg('cpc_f2013'))
        x.append('CCSH')
        x.append(anocpc)
        x.append(cpc_ccsh['cpc_f2013__avg'])
        if cpc_ccsh['cpc_f2013__avg'] is not None : d2.append(x)
        x = []

    #   cpc_ccs = cpc_centro.filter(centro = "CCS").aggregate(Avg('cpc_f2013'))
        cpc_ccr = cpc_centro.filter(centro = "CCR").aggregate(Avg('cpc_f2013'))
        x.append('CCR')
        x.append(anocpc)
        x.append(cpc_ccr['cpc_f2013__avg'])
        if cpc_ccr['cpc_f2013__avg'] is not None : d2.append(x)
        x = []

        cpc_ccne = cpc_centro.filter(centro = "CCR").aggregate(Avg('cpc_f2013'))
        x.append('CCNE')
        x.append(anocpc)
        x.append(cpc_ccne['cpc_f2013__avg'])
        if cpc_ccne['cpc_f2013__avg'] is not None :d2.append(x)
        x = []

        cpc_ctism = cpc_centro.filter(centro = "CTISM").aggregate(Avg('cpc_f2013'))
        x.append('CTISM')
        x.append(anocpc)
        x.append(cpc_ctism['cpc_f2013__avg'])
        if cpc_ctism['cpc_f2013__avg'] is not None :d2.append(x)
        x = []

        cpc_ce = cpc_centro.filter(centro = "CE").aggregate(Avg('cpc_f2013'))
        x.append('CE')
        x.append(anocpc)
        x.append(cpc_ce['cpc_f2013__avg'])
        if cpc_ce['cpc_f2013__avg'] is not None : d2.append(x)
        x = []

    #    cpc_cesnorspm = cpc_centro.filter(centro = "CESNORS PM").aggregate(Avg('cpc_f2013'))

    #    cpc_udssm = cpc_centro.filter(centro = "UDSSM").aggregate(Avg('cpc_f2013'))

        cpc_cal = cpc_centro.filter(centro = "CAL").aggregate(Avg('cpc_f2013'))
        x.append('CAL')
        x.append(anocpc)
        x.append(cpc_cal['cpc_f2013__avg'])
        if cpc_cal['cpc_f2013__avg'] is not None : d2.append(x)
        x = []

        cpc_ct = cpc_centro.filter(centro = "CT").aggregate(Avg('cpc_f2013'))
        x.append('CT')
        x.append(anocpc)
        x.append(cpc_ct['cpc_f2013__avg'])
        if cpc_ct['cpc_f2013__avg'] is not None : d2.append(x)

        anocpc = anocpc - 1

    print d2

    d2 = nr = sorted(d2, key=lambda x: x[2], reverse = True)

    return {'d1':d1, 'd2':d2, 'cpc':cpc, 'centros':centros,
            'ccne':ccne, 'cesnorsfw':cesnorsfw, 'cefd':cefd,
            'ccsh':ccsh, 'ccs': ccs, 'ccr':ccr, 'ctism':ctism,
            'ce':ce, 'cesnorspm':cesnorspm, 'udssm':udssm, 'cal':cal,
            'ct':ct, 'cursosmenu':cursosmenu, 'centrosmenu':centrosmenu}

def flocalizacao(cod_curso):
    latitude = []
    longitude = []
    localizacao = []
    query = MATRICULADOS_SISU.objects.all().filter(codigo_curso = cod_curso).values('municipio')

    for i in query:
        aux = MUNICIPIOS.objects.all().filter(MUNICIPIO = i.values()[0]).values('LATITUDE', 'LONGITUDE')
        if aux.exists():
            localizacao.append(aux.first())
        #latitude.append(aux.values('LATITUDE').first())
        #longitude.append(aux.values('LONGITUDE').first())

    return {'localizacao': localizacao}
