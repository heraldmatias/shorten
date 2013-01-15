# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
#from django.contrib import admin

urlpatterns = patterns('',
    # Example:
    # (r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:

    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^', include('home.urls')),
    #(r'^administrator/banner/', include('banner.urls_admin')),
    # Uncomment the next line to enable the admin:
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    #     {'document_root': settings.MEDIA_ROOT}),
    #url(r'^captcha/', include('captcha.urls')),
    #(r'^admin/', include(admin.site.urls)),

    #(r'^cms/', include(cms.urls)),
    # grapelli admin urls
    #(r'indice-tematico/',include("indice_tematico.urls")),
    

    #url(r'^(?P<url>[a-zA-Z0-9-/]+)/$','menu.views.ver_contenido_menu', name='inei-menulateral-tematico'),
)

#if settings.DEBUG:
from django.views.static import serve
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$',
        serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^static/(?P<path>.*)$',
        serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^favicon\.ico$',
        'django.views.generic.simple.redirect_to',
        {'url': '/static/images/favicon.ico'}),
)
