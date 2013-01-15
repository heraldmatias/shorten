# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from forms import LoginForm, ReporteForm, ReporteTable
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from datetime import datetime
from django.contrib.sites.models import get_current_site
from django.conf import settings
from home.models import Reporte
from urllib2 import urlopen
from django.contrib import messages
from django_tables2.config import RequestConfig

def internal_error_view(request):
    return render_to_response('500.html',{},context_instance=RequestContext(request))

def index(request):
    form = LoginForm()
    if 'next' in request.GET:
        return render_to_response('home/index.html', {'form': form,
            'login':'login','permission':False}, 
            context_instance=RequestContext(request),)
    return render_to_response('home/index.html', {'form': form,
        'login':'login'}, context_instance=RequestContext(request),)

def singin(request):
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['clave']
    try:        
        user = authenticate(username=username, password=password)
    except:
        user = None    
    if user is not None:
        if user.is_active:
            login(request, user)
            today = datetime.now() #fecha actual
            request.session['login_date'] = today
            request.session['nombres'] = user.get_full_name()
            return redirect('shorten-main')
        else:    
            form = LoginForm()
            return render(request,
                        "home/index.html",
                        {"error_message":"Su cuenta esta inactiva, porfavor consulte con su Administrador.",
                        'form':form,
                        'login':'login'})
    else:
        form = LoginForm()
        return render(request,
                        "home/index.html",
                        {"error_message":"Por favor ingrese valores correctos.",'form':form,'login':'login'})

@login_required()
def main(request): 
    if 'm' in request.GET:
        return render_to_response('home/home.html',{'m':request.GET['m']}, context_instance=RequestContext(request),)
    else: 
        return render_to_response('home/home.html', context_instance=RequestContext(request),)

@login_required()
def singout(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

@login_required()
def documentos_add(request, codigo=None):
    obj=None
    short_url = None
    if codigo:
        obj= get_object_or_404(Reporte,pk=codigo)        
    if request.method == 'POST':
        if 'archivo' in request.FILES:
            archivo = request.FILES['archivo']
            extension = archivo.name[archivo.name.rfind('.')+1:].upper()            
            filename= "%s%s.%s" % ('REPORTE-',datetime.today().strftime("%d%m%Y"),extension)            
            if not obj:
                obj = Reporte(usuario=request.user)            
            request.FILES['archivo'].name = filename
        filename = obj.archivo
        formulario = ReporteForm(request.POST,request.FILES,instance=obj ) # A form bound to the POST data
        if formulario.is_valid():
            if codigo and 'archivo' in request.FILES:
                FileSystemStorage().delete(filename)
            formulario.save()            
            bitly_url = "http://api.bit.ly/v3/shorten?login={0}&apiKey={1}&longUrl={2}&format=txt"
            req_url = bitly_url.format('o_1r4i8j6ca1',
                'R_bf0a523274308dc57ae0638c6799ac56',
                'https://docs.google.com/viewer?url=http://%s%s&embedded=true'%(request.META['HTTP_HOST'],obj.archivo.url))
            obj.short_url = urlopen(req_url).read()
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'Reporte grabado exitosamente!!!')
            #print "AQUI"
            #return redirect('shorten-mantenimiento-doc-query')
            short_url = obj.short_url
            obj = None
            formulario = ReporteForm()
    else:        
        formulario = ReporteForm(instance=obj)
    return render_to_response('home/agregar_reporte.html', {
        'reporte':obj,
        'short_url' : short_url,
        'formulario': formulario,},context_instance=RequestContext(request),)

@login_required()
def documentos_query(request):
    col = "-organismo"
    query = None
    dependencia=''
    usuario = ''
    filtro = list()
    if "2-sort" in request.GET:
        col = request.GET['2-sort']
    config = RequestConfig(request)
    #formulario = ConsultaDocumentoForm(request.GET)    
    tabla = ReporteTable(Reporte.objects.all())
    config.configure(tabla)
    tabla.paginate(page=request.GET.get('page', 1), per_page=6)
    return render_to_response('home/consultar_reporte.html',
        {#'formulario': formulario,
        'tabla':tabla,
        'dependencia':dependencia,
        'usuario':usuario}, context_instance=RequestContext(request),)

@login_required()
def documentos_print(request):
    col = "-organismo"
    query = None
    dependencia=''
    usuario = ''
    filtro = list()
    if "2-sort" in request.GET:
        col = request.GET['2-sort']
    config = RequestConfig(request)
    formulario = ConsultaDocumentoForm(request.GET)
    if 'organismo' in request.GET:
        if request.GET['organismo']:
            filtro.append(u"documentos.organismo_id =%s"%request.GET['organismo'])
        if 'dependencia' in request.GET:
            if request.GET['dependencia']:
                filtro.append(u"documentos.dependencia =%s"%request.GET['dependencia'])
                dependencia=request.GET['dependencia']
    if 'idusuario_creac' in request.GET:
        if request.GET['idusuario_creac']:
            filtro.append(u"idusuario_creac_id =%s"%request.GET['idusuario_creac'])
            usuario=request.GET['idusuario_creac']
    if 'categoria' in request.GET:
        if request.GET['categoria']:
            filtro.append(u"categoria ='%s'"%request.GET['categoria'])
    if 'tipo' in request.GET:
        if request.GET['tipo']:
            filtro.append(u"tipo ='%s'"%request.GET['tipo'])
    query = Reporte.objects.extra(where=filtro,select={'dependencia':"case documentos.organismo_id when 1 then (select ministerio from ministerio where nummin=documentos.dependencia) when 2 then (select odp from odp where numodp=documentos.dependencia) when 3 then (select gobernacion from gobernacion where numgob=documentos.dependencia) end"})
    html = render_to_string('extras/reporte_doc.html',{'data': query,'pagesize':'A4','usuario':request.user.get_profile()},context_instance=RequestContext(request))
    filename= "doc_%s.pdf" % datetime.today().strftime("%Y%m%d")        
    return imprimirToPDF(html,filename)