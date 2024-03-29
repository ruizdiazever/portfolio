from django.db import models
from django.db.models import FloatField
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(verbose_name="Titulo", blank=True, max_length=150)
    subtitle = models.CharField(verbose_name="Subtitulo", blank=True, max_length=150, default="Nea")
    year = models.CharField(max_length=4, verbose_name="Año", null=True, blank=True)
    text_time = models.CharField(max_length=6, verbose_name="Fecha")
    description = RichTextField(verbose_name="Descripcion", blank=True, null=True)
    #datetime = models.DateTimeField(verbose_name="Datetime", auto_now=False, blank=True)
    ordering = FloatField(verbose_name='Orden', default=0)
    link = models.URLField(null=True, blank=True)
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


class Curriculum(models.Model):
    title = models.CharField(verbose_name="Titulo", blank=True, max_length=30)
    file = models.FileField(upload_to='curriculum/')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def save(self, *args, **kwargs):
        try:
            this = Curriculum.objects.get(id=self.id)
            if this.file != self.file:
                this.file.delete()
        except: pass
        super(Curriculum, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Curriculum"
        verbose_name_plural = "Curriculum"
    
    def __str__(self):
        return self.title

class Docs(models.Model):
    title = models.CharField(verbose_name="Titulo", blank=True, max_length=20)
    subtitle = models.CharField(verbose_name="Subtitulo", blank=True, max_length=20, default="Nea")
    description = models.TextField(verbose_name="Descripcion", blank=True, null=True)
    link = models.URLField(null=True, blank=True)
    ordering = FloatField(verbose_name='Orden', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = "Docs"
        verbose_name_plural = "Docs"
        ordering = ['-ordering','created']
    
    def __str__(self):
        return self.title
