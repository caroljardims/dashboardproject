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
    url(r'^general', 'data.views.general', name='Geral UFSM'),
    url(r'^source/([0-9]*)/$', 'data.views.origemAlunos', name='origem_alunos'),
]
