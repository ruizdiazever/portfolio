from django.db import models
from django.db.models import SmallIntegerField
from ckeditor.fields import RichTextField

class Projects(models.Model):
    image = models.ImageField(upload_to="projects/card", verbose_name="Card image", null=True, blank=True)
    screen = models.ImageField(upload_to="projects/modal", verbose_name="Modal image", null=True, blank=True)
    title = models.CharField(max_length=50, verbose_name="Titulo")
    subtitle = models.CharField(max_length=50, verbose_name="Subtitulo", null=True)
    staff = models.CharField(max_length=120, verbose_name="Staff tecnologico", null=True)
    description = RichTextField(verbose_name="Descripcion")
    link = models.URLField(null=True, blank=True, verbose_name="GitHub")
    ordering = SmallIntegerField(verbose_name='Orden', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def save(self, *args, **kwargs):
        try:
            this = Projects.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except: pass
        super(Projects, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['ordering','created']
    
    def __str__(self):
        return self.title