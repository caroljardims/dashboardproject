# -*- coding:utf-8 -*-
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
from data.functions import *

tsg = TSG.objects.all()
cpc = CPC.objects.all().order_by("ano")
igc = IGC.objects.all().order_by("ano")

def index(request):
    context = geralufsm()
    return render_to_response('index.html', context)

def igc(request):
    context = figc()
    return render_to_response('igc.html', context)

def centros(request):
    context = fcursos()
    return render(request,"centros.html", context)

def centro(request, cod_centro):
    context = fcentro(cod_centro)
    return render(request,"centro.html", context)

def curso(request, cod_curso):
    context = fcurso(cod_curso)
    return render(request,"curso.html", context)

def list(request):
	context = fcursos()
	return render(request,"enade.html", context)

def avaliacaoCurso(request, cod_curso):
	context = favaliacao(cod_curso)
	return render(request, "avaliacao.html", context)

def listaCursos(request):
    context = fcursos()
    return render(request, "origin.html", context)

def origemAlunos(request, cod_curso):
    context = flocalizacao(cod_curso)
    return render(request, "source.html", context)