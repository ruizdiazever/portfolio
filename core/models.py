from django.db import models
from django.db.models import FloatField


class Blog(models.Model):
    year = models.CharField(max_length=4, verbose_name="Año", null=True, blank=True)
    datetime = models.DateTimeField(verbose_name="Datetime", auto_now=False, blank=True)
    text_time = models.CharField(max_length=6, verbose_name="Fecha")
    title = models.TextField(verbose_name="Titulo", blank=True)
    link = models.URLField(null=True, blank=True)
    ordering = FloatField(verbose_name='Orden', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog"
        ordering = ['-ordering','created']
    
    def __str__(self):
        return self.title

class Certificates(models.Model):
    title = models.TextField(verbose_name="Titulo", blank=True)
    image = models.ImageField(upload_to="certifications", verbose_name="Imagen", null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    ordering = FloatField(verbose_name='Orden', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"
        ordering = ['-ordering','created']
    
    def __str__(self):
        return self.title
