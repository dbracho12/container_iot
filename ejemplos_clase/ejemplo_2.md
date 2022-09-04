# Ejemplos de clase

En esta práctica continuaremos explorando el funcionamiento de Docker.

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

### 1 - Vistazo del contenedor de Python
Volver a lanzar el contenedor:
```sh
$ docker run -it python:3.9.1 bash
```

Verifique dónde está posicionada la consola:
```sh
$ ls -l
```

Ingresar a la carpeta home y crear un archivo app.py
```sh
$ cd home
$ touch app.py
```

Verificar que dentro de la carpeta home de la VM no existe esta nuevo archivo app.py
¿Qué curioso, cierto? ¿Dónde cree que estará ese archivo y que pasa cuando detenemos un contenedor?

### 2 - Ver las librerias instaladas en pip
Analizar que librerías están instaladas de python por defecto en el contenedor:
```sh
$ python3 -m pip list
```

Instalar Flask:
```sh
$ python3 -m pip install flask==2.0.3
```

Verificar nuevamente que librerías hay instaladas en el contenedor:
```sh
$ python3 -m pip list
```

### 3 - Lanzar un servidor flask simple
Editar el archivo "app.py" creado en los primeros pasos para lanzar una demostración simple de Flask. 

Instalar nano en el contenedor:
```sh
$ apt-get update
$ apt-get install nano
```

Utilice nano para abrir el archivo para editarlo:
```sh
$ nano app.py
```

Agregue el siguiente contenido:
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>¡Hola mundo!</h1>"

if __name__ == "__main__":
    app.run("0.0.0.0", 5030)
```

Salvar el archivo con "CTRL+S" y salir con "CTRL+X"

Lanzar el servidor con:
```sh
$ python3 app.py
```

Intente ingresar a la URL indicada en la terminal, mismo intente ingresando también con la IP de la VM.

No funciona, ¿cierto? --> ¡Correcto! Ya veremos por qué

### 4 - Cerrar el contenedor y volverlo a crear
Para cerrar el contenedor puede hacerlo con "CTRL+D" en la terminal del contenedor, o puede hacerlo en la terminal de la VM con:
```sh
$ docker ps
$ docker stop <container_id>
```

Volver a lanzar el contenedor:
```sh
$ docker run -it python:3.9.1 bash
```

Es un nuevo contenedor, ¿cierto? Observar el container_id:
```sh
$ docker ps
```

Observar las librerías instaladas:
```sh
$ python3 -m pip list
```

Observar el contenido del la carpeta home:
```sh
$ cd home
$ ls -l
```

¿Se perdió todo?

### 5 - Conclusiones
- Todo los archivos o librerías que se instalen dentro de un contenedor se perderán cuando este se detenga o se borre.
- Esto, a pesar de verse en principio como una desventaja, es una gran ventaja. Permite mantener a los sistemas limpios de toda modificación realizada post lanzamiento.
- Permite a su vez mantener aislado el contenedor de cambios.

Para agregar archivos o modificaciones permanentes deberemos agregarlas durante la creación de una imagen a medida (custom)
