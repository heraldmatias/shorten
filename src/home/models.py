# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Reporte(models.Model):
	codigo = models.AutoField(primary_key=True)
	archivo = models.FileField(verbose_name='Archivo',
		upload_to='reportes'
	)
	short_url = models.URLField(verbose_name='short_url',
		null=True, blank=True)
	descripcion = models.TextField(verbose_name='Descripción',
		null=True, blank=True)
	fec_creac = models.DateField(verbose_name='Fecha',)
	usuario = models.ForeignKey(User)