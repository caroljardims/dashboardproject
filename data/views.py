# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.forms.models import modelformset_factory
from data.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import unicodedata

tsg = TSG.objects.all()
cpc = CPC.objects.all().order_by("ano")
igc = IGC.objects.all().order_by("ano")

def index(request):
    context = {}
    return render_to_response('index.html', context)


def igc_ufsm(request):
    context = {}
    igc_ufsm = IGC.objects.all().filter(nomeies = "UNIVERSIDADE FEDERAL DE SANTA MARIA").order_by("ano")
    context = {'ufsm':igc_ufsm}

    return render_to_response('igc.html', context)


def centros(request):
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

    context = {'d1':d1, 'd2':d2}
    return render_to_response('centros.html', context)

def cursos(request):
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

    context = {'centros':centros, 'd1':d1}
    return render(request,"cursos.html", context)