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

def index(request):

    cpc = CPC.objects.all().order_by('area')
    tsg = TSG.objects.all()
    areas = []
    centros = []
    d1 = []

    for t in tsg:
       centros.append(t.centro)
    centros = list(set(centros))
    for c in centros:
        x = []
        for t in tsg:
            if c == t.centro:
                x.append(t)
        d1.append(x)

    for d in cpc:
       areas.append(d.area)
    areas = list(set(areas))
    for a in areas:
        x = []
        for d in cpc:
            if a == d.area:
                x.append(d)
                #print d.area
    #d1.append(x)
    # for a in areas: print a.encode('ascii','ignore')

    context = {'d1':d1}
    return render_to_response('index.html', context)

def centros(request):
    tsg = TSG.objects.all()
    centros = []
    d1 = []

    for t in tsg:
       centros.append(t.centro)
    centros = list(set(centros))
    for c in centros:
        x = []
        for t in tsg:
            if c == t.centro:
                x.append(t)
        d1.append(x)
    context = {'d1':d1}
    return render_to_response('centros.html', context)