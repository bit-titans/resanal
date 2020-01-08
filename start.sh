#!/usr/bin/env bash
sudo service nginx start
cd /app
sudo gunicorn -w 3 --bind unix:resnal.sock -m 007  resanalDjango.wsgi