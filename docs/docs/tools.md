* [Diagrams](https://app.diagrams.net): herramienta para diseñar diagramas en HTML.

* [Ckeditor](https://pypi.org/project/django-ckeditor/): usamos esta herramienta para poner opciones de edicion en textos.  

1- Instalar paquete en nuestro entorno virtual.
```path
$ pip install django-ckeditor
```

2- Agregar ```ckeditor``` en ```INSTALLED_APPS``` settings.py.

3- Agregar configuracion al final en settings.py.
```python
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    }
}
```