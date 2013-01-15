# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
#from django.contrib.auth.views import password_reset, password_reset_done,password_reset_confirm,password_reset_complete
#from forms import PasswordResetFormHtml
urlpatterns = patterns('home.views',
    url(r'^$','index', name='shorten-index'),
    url(r'^inicio/$','main', name='shorten-main'),
    url(r'^login/$','singin', name='shorten-login'),    
    url(r'^logout/$','singout', name='shorten-logout'),
    url(r'^reportes/add/$','documentos_add', name='shorten-mantenimiento-doc-add'),
    url(r'^reportes/edit/(?P<codigo>\d+)/$','documentos_add', name='shorten-mantenimiento-doc-edit'),
    url(r'^reportes/consulta/$','documentos_query', name='shorten-mantenimiento-doc-query'),
    url(r'^reportes/print/$','documentos_print', name='shorten-mantenimiento-doc-print'),
    #url(r'^accounts/password/reset/$', password_reset,{'template_name':'home/cambiar_clave.html','email_template_name':'home/email_cambio_clave.html','password_reset_form':PasswordResetFormHtml,'extra_context':{'login':'login'}},name='shorten-reset-pass'),
    #url(r'^accounts/password/reset/done/$', password_reset_done,{'template_name':'home/cambiar_clave_hecho.html','extra_context':{'login':'login',}} ,name='shorten-reset-done'),
    #url(r'^accounts/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,{'template_name':'home/cambiar_clave_confirma.html','extra_context':{'login':'login'}},name='shorten-reset-confirm'),
    #url(r'^accounts/password/done/$', password_reset_complete,{'template_name':'home/cambiar_clave_completado.html','extra_context':{'login':'login'}},name='shorten-reset-complete'),
    #url(r'^calendar/$','view_calendar', name='shorten-calendar'),
)
