# Django web app deploy to Heroku
Documentacion para el deployment de una web app de Django previamente dockerizada para la plataforma Heroku con el metodo Container Registry de la misma.

## **Primeros pasos**
- Registrarse en [**Heroku**](https://signup.heroku.com/)
- Crear app en el [**Dasboard**](https://dashboard.heroku.com/apps)

## **Preparacion del proyecto**
**En nuestro proyecto creamos los siguientes 3 archivos y añadimos a las mismas:**

```Procfile```, no lleva extension, agregamos la siguiente linea.
```
web: gunicorn docker_django_heroku.wsgi — log-file -
```
```runtime.txt```, agregamos la versión de Python que deseamos para nuestro proyecto.
```
python-3.9.1
```
```requirements.txt```, agregamos las librerias pip necesarias.
```
dj_database_url
gunicorn
django-heroku
```

**Editamos nuestro ```Dockerfile``` y agregamos lo siguiente al final**
``` 
CMD python manage.py runserver 0.0.0.0:$PORT
```


**La estructura de nuestro proyecto deberia ser algo parecido a esto:**
```code
📦webapp  
    ┣ 📂webapp  
    ┣ 📂core  
    ┣ 📜docker-compose.yml  
    ┣ 📜Dockerfile  
    ┣ 📜manage.py  
    ┣ 📜Procfile 
    ┣ 📜requirements.txt  
    ┗ 📜runtime.txt
```

## **Docker**
**Construimos nuestra imagen docker y la levantamos:**
```bash
$ sudo docker-compose -f docker-compose.yml build  # BUILD
$ sudo docker-compose -f docker-compose.yml up -d  # UP
$ sudo docker ps ls                                # CHECKING
```

## **Deploy**
**En nuestro Dasboard vamos a la seccion "Deploy" y hacemos click sobre el metodo "Container Registry", instalamos "Heroku CLI". Una vez hecho esto volvemos a nuestro proyecto y con el bash en el proyecto procedemos con los siguientes comandos:**
```bash
$ heroku login
$ docker ps
$ heroku container:login
$ heroku container:push web --app "<nameapp>"
$ heroku container:release web --app "<nameapp>"

# Nota: la "nameapp" debe ser la misma que la app creada en Heroku.
# Nota: el comando "docker ps" es para ver que los contenedores esten activos.
```

Si todo hubiera marchado bien ahora deberiamos tener nuestra web activa, comprobar la misma con el boton "Open app" en el Dashboard de Heroku.
