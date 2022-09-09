# Ejemplos de clase

En esta práctica crearemos nuestra propia imagen definitiva del iotbridge con docker, y la subiremos a nuestro dockerHub.

Para eso usted debe primero haberse creado una cuenta en dockerHub para continuar con esta práctica:
```
https://hub.docker.com/
```

Logearse desde VM y obtener cual es la dirección IP del dispositivo:
```sh
$ ifconfig
```

### 1 - Preparar el entorno de trabajo
Para poder realizar esta práctica, debe tener funcionando el ejemplo en donde se contruyó el iotbrige, a fin de que usted pueda subir es imagen generada con su nombre de usuario incoporado a su dockerhub.

### 2 - Subir la imagen a dockerhub
Puede buscar el nombre de la imagen deseada a subir con:
```sh
$ docker image list
```

Subir imagen a dockerhub que corresponde a su usuario (lleva el nombre de su usuario de dockerhub.)
```sh
$ docker push <usuario_dockerhub>/iotbridge:latest
```

Utilice todas las herramientas a su disposición (terminal, MQTTExplorer, debugger) para ensayar y testear el funcionamiento de su implementación. En caso que tenga problemas, consulte y continue explorando. Lo más rico de estos ejercicios es que pueda analizar las fallas y aprender de ellas por su cuenta como todo un buen detective.

Una vez finalizado el ejercicio y corroborado el funcionamiento, dejarnos en el comentario del campus de esta tarea el link a su imagen disponible en su dockerhub.
