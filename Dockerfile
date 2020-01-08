FROM python:3.6-slim
COPY requirements.txt /app/
WORKDIR /app

RUN apt-get clean \
    && apt-get -y update
RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential

RUN pip install -r requirements.txt

COPY nginx.conf /etc/nginx
CMD sudo service nginx start && sudo gunicorn -w 3 --bind unix:resnal.sock -m 007  resanalDjango.wsgi