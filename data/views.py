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

def index(request):
    context = geralufsm()
    return render_to_response('index.html', context)

def general(request):
    context = geralufsm()
    return render_to_response('general.html', context)

def centros(request):
    context = fcursos()
    return render(request,"centros.html", context)

def centro(request, cod_centro):
    context = fcentro(cod_centro)
    return render(request,"centro.html", context)

def curso(request, cod_curso):
    context = fcurso(cod_curso)
    return render(request,"curso.html", context)

def origemAlunos(request, cod_curso):
    context = flocalizacao(cod_curso)
    return render(request, "source.html", context)