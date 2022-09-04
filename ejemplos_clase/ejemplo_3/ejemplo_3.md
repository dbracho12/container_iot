# Ejemplos de clase

- Como vimos en uno de los ejemplos anteriores, nuestro contenedor con Flask no era capaz de ser accedido desde afuera (en la VM o en nuestra máquina) y cada vez que borramos el contenedor se pierde todo el contenido.
- En esta práctica crearemos nuestra propia imagen de Docker.

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

Para estar práctica se recomienda tener el VSC abierto (open folder) en la carpeta "ejemplo_3" que se encuentra dentro de "ejemplos_clase".

### 2 - Vistazo desde donde comenzamos
Esta carpeta es como normalmente se verá un repositorio con docker, tendrá:
- El infaltable archivo README (que sería ejemplo_3.md) explicando como funciona o ejecutar el sistema.
- Un archivo de docker-compose.yml (opcional) para lanzar el o los contenedores de este repositorio.
- Una carpeta por cada aplicación/servicio que será contenerizado. En este caso está la carpeta "flask_demo" con el mismo código que el ejemplo anterior.
- Dentro de cada carpeta de aplicación habrá un Dockerfile que será el cual utilicemos para crear nuestra imagen custom.


### 3 - Crear una imagen de Docker
Dentro de la carpeta "flask_demo" hay un archivo Dockerfile vacio, el cual iremos completando.

Primer comenzaremos por especificar arriba de todo desde que imagen parte esta nueva imagen custom, en este caso partiremos de la imagen de python que descargamos del docker hub. Copiar en el Dockerfile:
```Dockerfile
# imagen base de python
FROM python:3.9.1
``

Por defecto los Dockerfile de python no tienen permitido escribir sus mensajes de logs en la consola. Para evitar esto agregamos al Dockerfile:
```Dockerfile
# habilitar los mensajes por consola
ENV PYTHONUNBUFFERED=1
```

Luego debemos instalar todas las dependencias del sistema o de python que deseemos. En este caso unicamente necesitaremos instalar flask. Para ejecutar un comando de consola en un Dockerfile debemos anteponer la palabra "RUN":
```Dockerfile
# instalar dependencias
RUN python3 -m pip install flask==2.0.3
```

Con todo lo necesario instalado, resta agregar los archivos que nos interesen de nuestro sistema la contenedor. Antes de eso debemos especificar en donde agregaremos esos archivos, cual será la carpeta donde estará alocada la aplicación. Para eso utilizamos la palabra "WORKDIR":
```Dockerfile
# definir la ubicacion de nuestros archivos
WORKDIR /home
```

Ahora si podemos copiar los archivos. La palabra "COPY" espera primero que le pasemos la ubicación de donde están los archivos en la VM respecto al Dockerfile, y la ubicación en donde los queremos colocar dentro del cotenedor:
- El primer punto que ven es porque le estamos diciendo que queremos agregar todo lo que esté junto a ese archivo Dockerfile (todos los archivos y carpetas al mismo nivel).
- El segundo punto es para indicarle a la imagen que deseamos copiar esos archivos en el WORKDIR antes definido.
```Dockerfile
# copiar archivos del app a la imagen
COPY . .
```

Por último, podemos especificar que acción o comando queremos que se ejecute cuando el contenedor creado a partir de esta imagen se lance. En este caso deseamos que python lance el servidor flask (app.py):
```Dockerfile
# lanzar la aplicación
CMD python3 app.py
```

Listo! Nuestro Dockerfile se encuentra completo.

### 4 - Buildear y lanzar
Con el Dockerfile listo el docker-compose tiene todo lo que necesita para funcionar. Hechemos un vistaso al docker-compose
- Primero se declara la versión del docker-compose ha utilizar.
- Luego se declaran todos los servicios o apps que se desean crear, dándoles un nombre a cada uno (en este caso usamos un nombre genérico "app").
- Luego vienen parámetros de configuración, como por ejemplo donde buscar el Dockerfile para esa app (build: ...) y que puertos enlazar entre el host y el contenedor.

Builder las aplicaciones ejecutando dentro de la carpeta ejemplo_3:
```sh
$ docker-compose build
```

Lanzar el o los contenedores con:
```sh
$ docker-compose up
```

Verá el mismo log que