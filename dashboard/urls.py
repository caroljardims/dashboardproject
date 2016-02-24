from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'data.views.index', name='index'),
    url(r'^index', 'data.views.index', name='index'),
    url(r'^cursos', 'data.views.cursos', name='cursos'),
    url(r'^curso/([0-9]*)/$', 'data.views.curso', name='curso'),
    url(r'^igc', 'data.views.igc', name='IGC UFSM'),

]
