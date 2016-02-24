from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'data.views.index', name='index'),
    url(r'^index', 'data.views.index', name='index'),
    url(r'^centros', 'data.views.centros', name='centros'),
    url(r'^centro/([0-9]*)/$', 'data.views.centro', name='centro'),
    url(r'^curso/([0-9]*)/$', 'data.views.curso', name='curso'),
    url(r'^igc', 'data.views.igc', name='IGC UFSM'),
    url(r'^enade', 'data.views.list', name='enade'),
	url(r'^avaliacao/([0-9]*)/$', 'data.views.avaliacaoCurso', name='avaliacao'),
]
