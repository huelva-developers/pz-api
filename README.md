# pz-api [![Requirements Status](https://requires.io/github/huelva-developers/pz-api/requirements.svg?branch=master)](https://requires.io/github/huelva-developers/pz-api/requirements/?branch=master)

Proyecto zero API

## Ejecución de la API modo desarrollador

### Crear entorno virtual para python 3 e instalar dependencias

```
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install -r requirements.txt
```

### Crear BD utilizando las migraciones de django

```
$ python manage.py migrate
```

### Crear usuario administrador

```
$ python manage.py createsuperuser
```

### Ejecutar API: monta la api por defecto en localhost:8000

```
$ python manage.py runserver
```
