from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'data.views.index', name='index'),
    url(r'index', 'data.views.index', name='index'),
    url(r'cpc/(?P<dado>[a-z]{2}/)', 'data.views.cpc', name='cpc'),
]
