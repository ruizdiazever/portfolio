from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    image = models.ImageField(upload_to="about", verbose_name="Imagen", null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name="Nombre")
    content = RichTextField(verbose_name="Descripcion")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    class Meta:
        verbose_name = "Descripcion"
        verbose_name_plural = "Descripciones"
        ordering = ['created']
    
    def __str__(self):
        return self.title