# -*- coding: utf-8 -*-
from django import forms
from home.models import Reporte
import django_tables2 as tables
import itertools

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=45, label='E-mail:',
        widget=forms.TextInput(attrs={
        	'placeholder':'Ingrese su usuario',
        	'style':'width:430px;height:15px;color:#141313'
        }),
    )
    clave = forms.CharField(max_length=40, label='Contraseña:',
    	widget=forms.PasswordInput(attrs={
    		'placeholder':'Ingrese su contraseña',
    		'style':'width:430px;height:15px;color:#141313'
    	}),
    )

class ReporteForm(forms.ModelForm):

	class Meta:
		model = Reporte
		exclude = ('usuario',)
		widgets = {
            'descripcion': forms.Textarea(attrs={'style':'width:90%','rows':'6'}),            
        }

class ReporteTable(tables.Table):
    item = tables.Column(empty_values=())
    archivo = tables.TemplateColumn("""<a href="{% url shorten-mantenimiento-doc-edit record.pk %}"
    	title="Modificar">{{record.archivo.url}}</a>""", orderable=True)
    short_url = tables.TemplateColumn(
    	"<a href='{{record.short_url}}' target='_blank' >{{record.short_url}}</a>",
    	verbose_name='URL')
    descripcion = tables.TemplateColumn("{{record.descripcion|truncatewords:15}}")
    fec_creac = tables.Column(orderable=True)
    usuario = tables.Column(orderable=True)

    def __init__(self, *args, **kwargs):
        super(ReporteTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count(1)        
    
    def render_item(self):
        return '%d' % next(self.counter)

    class Meta:
        attrs = {"class": "table table-bordered table-condensed table-striped"}
        orderable = False
