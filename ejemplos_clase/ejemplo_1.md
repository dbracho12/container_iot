# Ejemplos de clase

### 1 - Preparar el entorno de trabajo

En esta práctica continuaremos explorando el funcionamiento de Docker.

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

Conectarse por ssh desde una terminal del host:
```
$ ssh inove@<ip_dispositivo>
```

Crear la carpeta "clase_6" para trabajar sobre los ejemplos de esta clase:
```sh
$ mkdir clase_6
```

Ingresar a la carpeta creada y clonar la carpeta del repositorio de esta clase:
```sh
$ cd clase_6
$ git https://github.com/InoveAlumnos/container_iot
$ cd container_iot
```

### 2 - Descargar y lanzar la imagen de python para Docker
Comencemos por descarga la imagen de python para Docker. Es probable que la descarga se realice rapidamente dado que esta imagen ya se utilizó en ejemplos anteriores:
```sh
$ docker pull python:3.9.1
```

Verificar que la imagen se ha desargado observando la lista de imagenes descargadas:
```sh
$ docker image list
```

Observar cuando pesa esta imagen y cuantos contenedores la están utilizando ahora:
```sh
$ docker system df -v
```

Verificar que contenedores de Docker están lanzados en este momento:
```sh
$ docker ps
```

Lanzar el contenedor a partir de la imagen de python con:
```sh
$ docker run -it python:3.9.1 bash
```

Verá como la terminal ha cambiado su nombre de usuario, esto indica que ahora nos encontramos en otro entorno. Abrir otra terminal en la VM:
```
$ ssh inove@<ip_dispositivo>
```

Verificar que efectivamente hay un contenedor lanzado:
```sh
$ docker ps
```

### 3 - Verificar la imagen de python descargada
Dentro de la terminal del contenedor verificar la versión de python del entorno ejecutando el siguiente comando:
```sh
$ python3 --version
```

Volver a la terminal abierta en la VM y verificar la versión de python del entorno ejecutando el siguiente comando:
```sh
$ python3 --version
```

Verá que cada entorno (la VM y el contenedor ejecutado dentro de la VM) tienen una versión de python distinta. Esto verifica que el contenedor está haciendo bien su trabajo.


### 4 - Detener el contenedor
Para detener el contedor debemos volver a la terminal dentro del contenedor y presionar "CTRL+D".

A continuación veremos que la terminal sale del contenedor y vuelve a ser una terminal de la VM normal.

Para verificar que no ha quedado ningún contenedor en ejecución ejecutamos:
```sh
$ docker ps
```

Para verificar los contenedores detenidos ejecutamos:
```sh
$ docker ps -a
```