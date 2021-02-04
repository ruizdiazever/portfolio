from django.db import models
from django.db.models import SmallIntegerField
from ckeditor.fields import RichTextField


class Projects(models.Model):
    image = models.ImageField(upload_to="projects", verbose_name="Imagen", null=True, blank=True)
    title = models.CharField(max_length=50, verbose_name="Titulo")
    state = models.CharField(max_length=50, verbose_name="Estado")
    description = RichTextField(verbose_name="Descripcion")
    link = models.URLField(null=True, blank=True)
    ordering = SmallIntegerField(verbose_name='Orden', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['ordering','created']
    
    def __str__(self):
        return self.title