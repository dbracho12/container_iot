# imagen base de python
FROM python:3.9.1

# habilitar los mensajes por consola
ENV PYTHONUNBUFFERED=1

# definir la ubicacion de nuestros archivos
WORKDIR /app

# instalar dependencias
RUN python3 -m pip install flask==2.0.3

# copiar archivos del app a la imagen
COPY . .

# lanzar la aplicación
CMD python3 app.py