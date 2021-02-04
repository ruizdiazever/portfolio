1- Creamos app ```about```  
```bash
$ python manage.py startapp about
```

2- Creamos nuestra template
```
about/
    |--templates/
                |--about/
                        |--about.html
```

2- Registramos nuestra app en el dasboard de Django con ```admin.py```
```python
from django.contrib import admin

# Importamos nuestro modelo
from .models import About 

# Declaramos campos de lectura
class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') 

# Registramos en el admin
admin.site.register(About, AboutAdmin) 
```

2- Registramos un nombre publico con ``` apps.py```
```python
from django.apps import AppConfig

class AboutConfig(AppConfig):
    name = 'about' # Predefinido al crear app
    verbose_name = 'Sobre mi' # Nombre publico, @Ever
```

3- Creamos nuestro model con el ORM de Django con ```models.py```
```python
from django.db import models

# Importamos Ckeditor, para implementarlo buscar en Tools
from ckeditor.fields import RichTextField 

class About(models.Model):
    # Con 'upload_to' indicamos en que carpeta de media guardamos 'image'
    image = models.ImageField(upload_to="about", verbose_name="Imagen", null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name="Nombre")
    # Usamos Ckeditor
    content = RichTextField(verbose_name="Descripcion")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = "Descripcion"
        verbose_name_plural = "Descripciones"
        ordering = ['created']
    
    def __str__(self):
        return self.title
```

4- Declaramos nuestras urls en ```urls.py```
```python
# Importamos path
from django.urls import path 
# Importamos views
from . import views

urlpatterns = [
    # Con 'name' llamamos en el template
    path('', views.about, name="about"),
]
```

5- Creamos nuestra vista en ```views.py```
```python
from django.shortcuts import render
from .models import About

def about(request):
    # Importantisimo para iterar los objetos del model en template
    about = About.objects.all()
    # Clave valor para iterar..
    return render(request, 'about/about.html', {'about':about})
```

5- Registramos nuestra app y sus configuraciones en  ```settings.py```
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'about.apps.AboutConfig', # ACA
    'bootstrap4',
    'ckeditor',
    'core',
    'projects',
]
```

5- Otras configuraciones manuales en ```settings.py```, al final de la misma
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```