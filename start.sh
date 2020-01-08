gunicorn -w 3 --bind unix:resnal.sock -m 777 resanalDjango.wsgi
service nginx start