# Invera ToDo-List Challenge (Python/Django Jr-SSr)
Aplicación web sencilla que permita a los usuarios crear y mantener una lista
de tareas.

# Tecnología usada
Desarrollada sobre Django 4.1.2 + Python 3.11.1. Utiliza una base de datos
Postgres. Incluye DjangoRestFramework para el desarrollo de las API's.

## Instalación en entorno local
Se necesita tener instalado Docker.
Clonar el repositorio y posicionarse en el directorio descargado
~~~
$ git clone https://github.com/wilmays10/todo-challenge
$ cd todo-challenge
~~~
Ejecutar el script 'init_local.sh'
~~~
$ ./init_local.sh
~~~

## Consideraciones
- No se creó un front end ya que no era requisito, por lo tanto las vistas de
  registro, login, y logout están en urls separadas y no aparecen unificadas en
  un sólo template.
- Para la autenticación, se usó la librería [dj-rest-auth](https://github.com/iMerica/dj-rest-auth)
- Se agregó un API de registro, por lo que no es necesario entrar al admin como
  superusuario. Usando esta API, se registra un usuario y se puede usar las
  demás API's. Para poder hacer este registro, se usó [django-allauth](https://github.com/pennersr/django-allauth)

## API's
- Tareas:
  http://localhost:8000/api/tareas/
- Registro:
  http://localhost:8000/api/registration/
- Login:
  http://localhost:8000/api/authentication/login/
- Logout
  http://localhost:8000/api/authentication/logout/