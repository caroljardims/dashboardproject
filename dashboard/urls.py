from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:

    url(r'^dashboard/admin/', include(admin.site.urls)),
    url(r'^$', 'data.views.index', name='index'),
    url(r'^$dashboard/', 'data.views.index', name='index'),
    url(r'^dashboard/index', 'data.views.index', name='index'),
    url(r'^dashboard/centros', 'data.views.centros', name='centros'),
    url(r'^dashboard/centro/([0-9]*)/$', 'data.views.centro', name='centro'),
    url(r'^dashboard/curso/([0-9]*)/$', 'data.views.curso', name='curso'),
    url(r'^dashboard/general', 'data.views.general', name='Geral UFSM'),
    url(r'^dashboard/source/([0-9]*)/$', 'data.views.origemAlunos', name='origem_alunos'),
]
