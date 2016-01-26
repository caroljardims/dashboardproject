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

	data = CPC.objects.all().order_by('area')
	areas = []

	d1 = []

	for d in data:
		areas.append(d.area)
	areas = list(set(areas))
	for a in areas:
		x = []
		for d in data:
			if a == d.area:
				x.append(d)
				print d.area
		d1.append(x)
	# for a in areas: print a.encode('ascii','ignore')

	context = {'d1':d1}
	return render_to_response('index.html', context)