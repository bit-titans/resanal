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
COPY start.sh /app/
RUN chmod +x ./start.sh
CMD ["sudo ./start.sh"]