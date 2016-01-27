from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'data.views.index', name='index'),
    url(r'index', 'data.views.index', name='index'),
    url(r'centros', 'data.views.centros', name='centros'),
]
