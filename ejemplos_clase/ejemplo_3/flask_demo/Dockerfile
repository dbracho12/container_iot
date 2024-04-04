FROM python:3.9.1
ENV PYTHONUNBUFFERED=1

RUN python3 -m pip install flask==2.0.3
RUN python3 -m pip install Werkzeug==2.2.2

WORKDIR /home
COPY . .

CMD python3 app.py