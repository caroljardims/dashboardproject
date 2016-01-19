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



    #############
    #           #
    #   Index   #
    #           #
    #############

def index(request):

	data = TSG.objects.all().order_by('NOMECURSO')

	chart = []
	centro = []
	tsgcentro = []
	for d in data:
		chart.append(d)
		if d.ANO == 2015:
			centro.append((d.CENTRO, d.TSGCENTRO))
	centro = list(set(centro))
	print centro

	context = {'data': data, 'chart':chart, 'centro':centro, 'tsgcentro':tsgcentro}
	return render_to_response('index.html', context)


def cpc(request, dado):
	data = CPC.objects.all().order_by('SIGLAIES')
	c = []
	for a in data:
		if dado == "sm/":
			if a.MUNICIPIOCURSO == "SANTA MARIA":
				c.append(a)
		elif dado == "fw/":
			if a.MUNICIPIOCURSO == "FREDERICO WESTPHALEN":
				c.append(a)
		else:
			if a.MUNICIPIOCURSO == "PALMEIRA DAS MISSOES":
				c.append(a)
	nome = None
	if dado == "sm/":
		nome = "SANTA MARIA"
	elif dado == "fw/":
		nome = "FREDERICO WESTPHALEN"
	else:
		nome = "PALMEIRA DAS MISSÕES"
	context = {'data':data, 'c':c, 'nome':nome}
	return render(request,'cpc.html', context)