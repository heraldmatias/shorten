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

class ArchivosReporte(models.Model):
    codigo = models.AutoField(primary_key=True)
    reporte = models.ForeignKey(Reporte,
    	null=True,blank=True,related_name='archivos')
    archivo1 = models.FileField(verbose_name='Adjuntar Archivo 1',
    	upload_to='reportes/archivos/',null=True,blank=True)
    archivo2 = models.FileField(verbose_name='Adjuntar Archivo 2',
    	upload_to='reportes/archivos/',null=True,blank=True)
    archivo3 = models.FileField(verbose_name='Adjuntar Archivo 3',
    	upload_to='reportes/archivos/',null=True,blank=True)
    archivo4 = models.FileField(verbose_name='Adjuntar Archivo 4',
    	upload_to='reportes/archivos/',null=True,blank=True)
    archivo5 = models.FileField(verbose_name='Adjuntar Archivo 5',
    	upload_to='reportes/archivos/',null=True,blank=True)
    archivo6 = models.FileField(verbose_name='Adjuntar Archivo 6',
    	upload_to='reportes/archivos/',null=True,blank=True)
    archivo7 = models.FileField(verbose_name='Adjuntar Archivo 7',
    	upload_to='reportes/archivos/',null=True,blank=True)
    archivo8 = models.FileField(verbose_name='Adjuntar Archivo 8',
    	upload_to='reportes/archivos/',null=True,blank=True)
    archivo9 = models.FileField(verbose_name='Adjuntar Archivo 9',
    	upload_to='reportes/archivos/',null=True,blank=True)
    archivo10 = models.FileField(verbose_name='Adjuntar Archivo 10',
    	upload_to='reportes/archivos/',null=True,blank=True)

    class Meta:
        db_table = u'reportes_archivos'
        verbose_name = u'ArchivoReporte'
        verbose_name_plural = u'ArchivosReporte'
        
    def __unicode__(self):
        return self.codigo