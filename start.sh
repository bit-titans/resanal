#!/usr/bin/env bash
service nginx start
cd /app
gunicorn -w 3 --bind unix:resnal.sock -m 007  resanalDjango.wsgi