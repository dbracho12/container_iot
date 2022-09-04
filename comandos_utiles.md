## Comandos básicos de Docker
Cómo descargar una imagen
```sh
$ docker pull <nombre_imagen>
```
Cómo lanzar un contenedor desde una imagen
```sh
$ docker run -it <nombre_imagen> bash
```
Cómo ver las imagenes descargadas
```sh
$ docker image list
```
Cómo ver el espacio opupadas por las imagenes
```sh
$ docker system df -v
```
Cómo borrar una imagen
```sh
$ docker rmi <nombre_imagen>
```
Cómo borrar todas las imagenes y contenedores
```sh
$ docker system prune -a
```
Cómo ver los contenedores lanzados
```sh
$ docker ps
```
Cómo ver todos los contenedores (los lanzados y los detenidos)
```sh
$ docker ps -a
```
Cómo detener un cotenedor
```sh
$ docker stop <container_id>
```
Cómo detener todos los contenedores
```sh
$ docker kill $(docker ps -q)
```

## Comandos básicos de docker-compose
Buildear las imagenes
```sh
$ docker-compose build
```
Lanzar los contenedores tomando la consola
```sh
$ docker-compose up
```
Lanzar los contenedores sin tomar la consola
```sh
$ docker-compose start
```
Detener los contenedores
```sh
$ docker-compose stop
```
Si se necesita forzar un rebuild desde cero
```sh
$ docker-compose build --no-cache
```
Borrar los contenedores generadores por este compose
```sh
$ docker-compose rm -f
```

