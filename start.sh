sudo gunicorn -w 3 --bind unix:resnal.sock -m 777  resanalDjango.wsgi
sudo service nginx start