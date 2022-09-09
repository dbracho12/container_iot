# Ejemplos de clase

En esta práctica crearemos nuestra propia imagen definitiva del iotbridge con docker, utilizaremos docker-compose para levantar toda la solución.

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

Para estar práctica se recomienda tener el VSC abierto (open folder) en la carpeta "ejemplo_4" que se encuentra dentro de "ejemplos_clase".


### 1 - Vistazo desde donde comenzamos
Esta carpeta es como normalmente se verá un repositorio con docker, tendrá:
- El infaltable archivo README (que sería ejemplo_4.md) explicando como funciona o ejecutar el sistema.
- Un archivo de docker-compose.yml (opcional) para lanzar el o los contenedores de este repositorio.
- Una carpeta por cada aplicación/servicio que será contenerizado. En este caso está la carpeta "iotbridge" y el repositorio de "prometheus"
- Dentro de cada carpeta de aplicación habrá un Dockerfile que será el cual utilicemos para crear nuestra imagen custom.

__NOTA__: Se agregaron algunas funcionalidades extra al programa de bridge que veniamos trabajando:
- La posibilidad de buscar las variables de entorno en un archivo en el sistema:
```python
config = dotenv_values()
if not config:
    # No existe el archivo .env
    # Leer de las variables de entorno
    config = dict(os.environ)
```
- Que bucle principal esté monitoreando los threads, y en caso de que uno falle cerrar la aplicación forzosamente:
```python
# ----------------------
# El programa principal queda a la espera de que se desee
# finalizar el programa
while flags["thread_continue"]:
    # Verificar si algún thread se cayó
    if flags["thread_continue"] == True:
        force_exit = False
        for thread in threads:
            if thread.is_alive() == False:
                logging.error(f"Thread: {thread} explotó!")
                force_exit = True

        if force_exit == True:
            sys.exit()
```

### 2 - Descargar prometheus
Dentro de esta carpeta de ejemplo_4, clonar el repositorio de prometheus:
```sh
$ git clone https://github.com/InoveAlumnos/prometheus_monitoreo
```

Lanzar el docker-compose solo con el prometheus para verificar que este fue correcamente descargado:
```sh
$ docker-compose build
$ docker-compose up
```

### 3 - Agregar el servicio de nuestra aplicación
Dentro de la carpeta encontraremos un docker-compose que ya está preparado para ejecutar unicamente el servicio de monitoreo (prometheus).

Primero comenzaremos por especificar debajo del servicio de prometheus el servicio del "iotbride" y donde encontar el Dockerfile correspondiente:
```Dockerfile
iotbridge:
  build: ./iotbridge
```

Debajo de la etiqueta build iremos agregando más detalles. En este caso especificaremos como deseamos que se llame la imagen que genere este docker-compose. Para eso debemos agregar la siguiente linea indicando su nombre de usuario de dockerHub:
```Dockerfile
image: <usuario_dockerhub>/iotbridge:latest
```

A continuació agregar la funcionalidad que permite al sistema reiniciarse cada vez que ocurra una falla:
```Dockerfile
restart: always
```

Agregar la funcionalidad que permite que el conteiner pueda acceder a nuestra red local y conectarse a MQTT:
```Dockerfile
network_mode: "host"
```

Conectar los volumenes que permitan alojar los logs de la aplicación en nuestro host (nuestra PC, la VM) para poder consultarlos si es encesario:
```Dockerfile
volumes: 
  - /home/logs/iotbridge:/home/logs/iotbridge
```

Por último, agregar el archivo de variables de entorno para que pueda utilizar el contenedor cuando se lance:
```Dockerfile
env_file:
  - .env
```

__IMPORTANTE__: Recuerde modificar el archivo .env con los datos de su usuario del campus.


### 4 - Lanzar el sistema completo
Primero de todo, buildear todas las imagenes definidas en el docker-compose:
```sh
$ docker-compose build
```

Lanzar el sistema completo:
```sh
$ docker-compose up
```

Si todos los contenedores se lanzaron correctamente, podrá ver como el sistema comienza a reportar el monitoreo de telemetría y le keepalive al dashboard.


### 4 - Ensayar el reset always
La funcionalidad de set always permitirá que en caso de que el contenedor se caiga porque algo fallo en la aplicación, este se vuelva a lanzar automaticamente.

Por ejemplo, enviemos un mensaje de texto al tópico de inerciales que espera un JSON String:
```sh
$ mosquitto_pub -t sensores/inerciales -m 1
```

Habrá observado como el contenedor falló (ocurrió una excepción) pero inmediatamente se lanzó uno nuevo. Esto lo puede ver ya que en el log vuelven a aparecer los mensajes de MQTT connect que se visualizacn al comienzo.